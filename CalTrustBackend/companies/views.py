from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import *
from .models import Company
from account.models import FirmProfile
from reviews.serializers import PublicReviewSerializer


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
            

class LatestCompanies(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        limit = request.query_params.get('limit', 8)  # Rend la limite configurable
        try:
            companies = Company.objects.all().order_by('-created_at')[:int(limit)]
            serializer = CompanySerializer(companies, many=True)
            return Response({
                'status': 'success',
                'count': len(serializer.data),
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, id):
        try:
            company = Company.objects.select_related(
                'name',
                'name__user'
            ).prefetch_related(
                'name__reviews',
                'name__reviews__customer',
                'name__reviews__customer__user',
                'name__reviews__response'
            ).get(id=id)
            
            serializer = CompanySerializer(company)
            stats = company.rating_stats
            
            return Response({
                "status": "success",
                "data": {
                    "company": CompanySerializer(company).data,
                    "reviews": { 
                        "count": company.review_count,
                        "average": company.average_rating,
                        "list": PublicReviewSerializer(
                            company.name.reviews.all(),
                            many=True
                        ).data
                    },
                    "stats": company.rating_stats
                }
            })
            
        except Company.DoesNotExist:
            return Response({
                'status': 'error',
                'message': "Entreprise non trouvée"
            }, status=status.HTTP_404_NOT_FOUND)

# Category section !!!

class CategoryListView(APIView):
    permission_classes = [AllowAny]
    """Liste toutes les catégories disponibles"""
    def get(self, request):
        return Response({
            'categories': Company.get_category_choices()
        })

class CompaniesByCategory(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, category):
        # Vérifie que la catégorie est valide
        if category not in dict(Company.CategoryChoices.choices):
            return Response(
                {'error': 'Catégorie invalide'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Récupère les entreprises de cette catégorie
            companies = Company.objects.filter(category=category).order_by('-created_at')
            
            # Pagination optionnelle
            limit = request.query_params.get('limit')
            if limit:
                try:
                    companies = companies[:int(limit)]
                except ValueError:
                    pass
            
            serializer = CompanySearchSerializer(companies, many=True)
            
            return Response({
                'status': 'success',
                'category': {
                    'value': category,
                    'label': dict(Company.CategoryChoices.choices)[category]
                },
                'count': companies.count(),
                'data': serializer.data
            })
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# views.py
class CompanySearchView(APIView):
    permission_classes = [AllowAny]
    """Recherche avancée d'entreprises"""
    def get(self, request):
        params = request.query_params
        filters = {
            'category': params.get('category'),
            'query': params.get('q'),
            'name': params.get('name')  # Nouveau paramètre pour la recherche par nom
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