from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from account.models import FirmProfile
from account.serializer import FirmProfileSerializer
from companies.models import Company
from companies.serializer import CompanyAsUser
from django.contrib.auth.models import User

class FirmProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Vérifie que l'utilisateur a bien un profil entreprise
        profile = get_object_or_404(FirmProfile, user=request.user)
        serializer = FirmProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = get_object_or_404(FirmProfile, user=request.user)
        serializer = FirmProfileSerializer(profile, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfile(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            
            response_data = {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date_joined": user.date_joined,
                }
            }

            if hasattr(user, 'account_customer_profile'):
                profile = user.account_customer_profile
                response_data["profile_type"] = "customer"
                response_data["profile_details"] = {
                    "phone": profile.phone,
                    "birth_date": str(profile.birth_date) if profile.birth_date else None
                }
            elif hasattr(user, 'firm_profile'):
                profile = user.firm_profile
                response_data["profile_type"] = "firm"
                response_data["profile_details"] = {
                    "company_name": profile.company_name,
                    "address": profile.address,
                    "is_verified": profile.is_verified,
                    "phone_number": profile.phone_number
                }
            else:
                return Response(
                    {"error": "Profil non trouvé pour cet utilisateur."},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(response_data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response(
                {"error": "Utilisateur non trouvé."},
                status=status.HTTP_404_NOT_FOUND
            )