from django.shortcuts import render, HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from account.models import FirmProfile
from rest_framework.permissions import AllowAny
from .serializer import CompanySerializer
from .models import Company

# Create your views here.

class FirmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmProfile
        fields = '__all__'

class MyFimrsUser(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        try:
            # Récupérer tous les objets FirmProfile
            firms = FirmProfile.objects.all()
            # Sérialiser le QuerySet
            serializer = FirmProfileSerializer(firms, many=True)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CompanyByCategory(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_code):
        try:
            # Vérifier que le code de catégorie est valide
            valid_categories = [choice[0] for choice in Company.CategoryChoices.choices]
            if category_code not in valid_categories:
                return Response({
                    'status': 'error',
                    'message': 'Catégorie invalide'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Filtrer les entreprises par catégorie
            companies = Company.objects.filter(category=category_code)
            serializer = CompanySerializer(companies, many=True)
            
            return Response({
                'status': 'success',
                'data': serializer.data,
                'category_name': dict(Company.CategoryChoices.choices).get(category_code)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)