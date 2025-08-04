from django.shortcuts import render, HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from account.models import FirmProfile
from rest_framework.permissions import AllowAny
from .serializer import CompanySearchSerializer

from .models import Company

# Create your views here.

class FirmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmProfile
        fields = '__all__'

class MyFirmsUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            # 1. Utilisez Company plutôt que FirmProfile pour avoir accès aux métriques
            companies = Company.objects.select_related('name')\
                                     .prefetch_related('reviews')\
                                     .order_by('-created_at')[:4]
            
            # 2. Sérialiseur adapté incluant les stats
            serializer = CompanySearchSerializer(companies, many=True)
            
            return Response({
                'status': 'success',
                'data': serializer.data  # Contient déjà rating/count
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': "Erreur de chargement des entreprises"
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