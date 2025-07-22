from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializer import UserRegistrationSerializer
from .models import *

# Create your views here.
def index (request):
    return HttpResponse("Bienvenu au pays ")

class UserRegistrationView(APIView):
    """
    API endpoint for user registration (customer or firm).
    """
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow any user to access
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if not serializer.is_valid():
            # Formatage des erreurs pour plus de clarté
            errors = {}
            for field, error_list in serializer.errors.items():
                errors[field] = error_list[0] if error_list else "Invalid value"
            return Response(
                {
                    "status": "error",
                    "message": "Validation failed",
                    "errors": errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user_profile = serializer.save()
            
            # Construction de la réponse
            response_data = {
                "status": "success",
                "message": "User and profile created successfully!",
                "data": {
                    "user": {
                        "username": user_profile.user.username,
                        "email": user_profile.user.email,
                        "user_type": "customer" if isinstance(user_profile, CustomerProfile) else "firm"
                    }
                }
            }
            
            # Ajout des détails spécifiques au type de profil
            if isinstance(user_profile, CustomerProfile):
                response_data["data"]["profile_details"] = {
                    "phone": user_profile.phone,
                    "birth_date": str(user_profile.birth_date) if user_profile.birth_date else None
                }
            elif isinstance(user_profile, FirmProfile):
                response_data["data"]["company_details"] = {
                    "company_name": user_profile.company_name,
                    "siret": user_profile.siret,
                    "address": user_profile.address,
                    "is_verified": user_profile.is_verified
                }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            # Gestion des erreurs inattendues
            return Response(
                {
                    "status": "error",
                    "message": "An error occurred during registration",
                    "detail": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
class PasswordResetConfirmView(APIView):
    def post(self, request, token):
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not new_password or not confirm_password:
            return Response({'error': 'Veuillez fournir un nouveau mot de passe et le confirmer.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_password:
            return Response({'error': 'Les mots de passe ne correspondent pas.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            password_reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            return Response({'error': 'Token invalide ❌'}, status=status.HTTP_400_BAD_REQUEST)

        # Vérifier l'expiration
        if password_reset_token.expires_at < timezone.now():
            return Response({'error': 'Token expiré ❌'}, status=status.HTTP_400_BAD_REQUEST)

        # Vérifier que le token correspond bien à un utilisateur valide
        if not password_reset_token.user.is_active:
            return Response({'error': 'Compte utilisateur inactif ou non valide ❌'}, status=status.HTTP_400_BAD_REQUEST)

        # Tout est bon, on peut modifier le mot de passe
        user = password_reset_token.user
        user.set_password(new_password)
        user.save()

        # Supprimer le token après utilisation
        password_reset_token.delete()

        return Response({'message': 'Mot de passe réinitialisé avec succès ✅'}, status=status.HTTP_200_OK)