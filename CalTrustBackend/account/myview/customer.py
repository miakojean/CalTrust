from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from account.models import CustomerProfile
from account.serializer import CustomerProfileSerializer
from django.contrib.auth.models import User
from companies.models import Company
from companies.serializer import CompanySerializer

class CustomerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Vérifie que l'utilisateur a bien un profil client
        profile = get_object_or_404(CustomerProfile, user=request.user)
        serializer = CustomerProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = get_object_or_404(CustomerProfile, user=request.user)
        serializer = CustomerProfileSerializer(profile, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompaniesList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Vérifie que l'utilisateur a bien un profil client
        if not hasattr(request.user, 'account_customer_profile'):
            return Response(
                {"error": "Accès réservé aux clients."},
                status=status.HTTP_403_FORBIDDEN
            )
            
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)