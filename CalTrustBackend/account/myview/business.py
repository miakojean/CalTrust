from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

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

            # Check if the user has a customer profile
            if hasattr(user, 'account_customer_profile'):
                profile = user.account_customer_profile
                response_data["profile_type"] = "customer"
                response_data["profile_details"] = {
                    "phone": profile.phone,
                    "birth_date": str(profile.birth_date) if profile.birth_date else None
                }
            # Check if the user has a firm profile
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