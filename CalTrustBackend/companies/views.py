from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import CompanySearchSerializer, CompanyAsUser
from .models import Company
from account.models import FirmProfile


# Create your views here.

class FirmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class MyCompanyUserAccount(APIView):
    """
    Vue pour créer ou mettre à jour l'entreprise d'un utilisateur authentifié.
    - POST: Crée une nouvelle entreprise pour l'utilisateur.
    - PUT: Met à jour l'entreprise existante de l'utilisateur.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Vérifiez si l'utilisateur a déjà un profil d'entreprise
        try:
            firm_profile = request.user.firm_profile
        except FirmProfile.DoesNotExist:
            return Response(
                {"detail": "Firm profile not found for this user."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Si une entreprise existe déjà pour ce profil, la création n'est pas possible
        if Company.objects.filter(name=firm_profile).exists():
            return Response(
                {"detail": "You already have a company. Use PUT to update it."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Le serializer reçoit les données de la requête
        serializer = CompanyAsUser(data=request.data)
        
        # Si les données sont valides
        if serializer.is_valid():
            # Le champ 'name' est automatiquement lié au FirmProfile de l'utilisateur
            serializer.save(name=firm_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # En cas d'erreur de validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """
        Récupère les informations de l'entreprise pour l'utilisateur authentifié.
        """
        try:
            # Récupère l'entreprise liée à l'utilisateur authentifié
            company_instance = Company.objects.get(name__user=request.user)
        except Company.DoesNotExist:
            return Response(
                {"detail": "Aucune entreprise n'est associée à cet utilisateur."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Sérialise l'instance trouvée
        serializer = CompanyAsUser(company_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            # Récupérer l'instance de l'entreprise de l'utilisateur authentifié
            company_instance = Company.objects.get(name__user=request.user)
        except Company.DoesNotExist:
            return Response(
                {"detail": "No company found for this user. Use POST to create one."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Mettre à jour l'entreprise existante avec les données de la requête
        serializer = CompanyAsUser(company_instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class MyFirmsUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            # 1. Utilisez Company plutôt que FirmProfile pour avoir accès aux métriques
            companies = Company.objects.all().order_by('-created_at')[:4]
            
            # 2. Sérialiseur adapté incluant les stats
            serializer = CompanySearchSerializer(companies, many=True)
            
            # 3 Ajouter si nécessaire le serialiser de firmProfile pour plus de données
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)  # Afficher l'erreur réelle pour le débogage
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryListView(APIView):
    permission_classes = [AllowAny]
    """Liste toutes les catégories disponibles"""
    def get(self, request):
        return Response({
            'categories': Company.get_category_choices()
        })

# views.py
class CompanySearchView(APIView):
    permission_classes = [AllowAny]
    """Recherche avancée d'entreprises"""
    def get(self, request):
        params = request.query_params
        filters = {
            'category': params.get('category'),
            'query': params.get('q')
        }
        
        # Gestion spécifique de min_rating
        min_rating = params.get('min_rating')
        if min_rating:
            try:
                filters['min_rating'] = float(min_rating)
            except (TypeError, ValueError):
                return Response(
                    {'error': 'min_rating doit être un nombre valide'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Validation de la catégorie
        if filters['category'] and filters['category'] not in dict(Company.CategoryChoices.choices):
            return Response(
                {'error': 'Catégorie invalide'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Recherche et sérialisation
        companies = Company.search(**filters)
        serializer = CompanySearchSerializer(companies, many=True)
        
        return Response({
            'count': companies.count(),
            'results': serializer.data
        })