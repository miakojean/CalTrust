from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .utils import generate_password_reset_token, send_password_reset_email
from django.utils import timezone
from django.conf import settings

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
                    "phone_number": user_profile.phone_number,
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
        
class UserLoginView(APIView):
    # Allow any user (authenticated or not) to access this view
    permission_classes = [AllowAny]
    # Do not require any authentication scheme for this view
    authentication_classes = [] # This is key!
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        if not password or (not email and not username):
            return Response(
                {'error': 'Veuillez fournir un email/nom d\'utilisateur et un mot de passe.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Si email est fourni, on cherche l'utilisateur par email
        if email:
            user = User.objects.filter(email=email).first()
            if not user:
                return Response(
                    {'error': 'Email ou mot de passe incorrect.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            username = user.username 

        # Authentification
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username
            })
        else:
            return Response(
                {'error': 'Identifiants incorrects.'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Seuls les utilisateurs authentifiés peuvent se déconnecter

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {'message': 'Deconnexion réussie'},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {'message': 'Un erreur est survenue lors de la connexion'},
                status=status.HTTP_400_BAD_REQUEST
            )

class PasswordResetRequestView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'Veuillez fournir une adresse e-mail.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'message': 'Si un compte existe, un email a été envoyé.'},
                status=status.HTTP_200_OK
            )

        # Génération et envoi délégués aux utils
        token = generate_password_reset_token(user)
        reset_link = f'{settings.FRONTEND_URL}/reset-password/{token}'  # Configurez FRONTEND_URL dans settings.py
        send_password_reset_email(user, reset_link)

        return Response(
            {'message': 'Si un compte existe, un email a été envoyé.'},
            status=status.HTTP_200_OK
        )

class PasswordResetTokenVerifyView(APIView):
    """
    Vérifie la validité d'un token de réinitialisation
    Exemple de requête : POST /api/password-reset/verify-token/
    {
        "token": "abc123..."
    }
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        token = request.data.get('token')
        
        if not token:
            return Response(
                {"valid": False, "message": "Token requis"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            reset_token = PasswordResetToken.objects.get(
                token=token,
                expires_at__gt=timezone.now()  # Vérifie que le token n'a pas expiré
            )
            return Response({
                "valid": True,
                "message": "Token valide",
                "email": reset_token.user.email  # Optionnel : pour confirmation frontend
            })
            
        except PasswordResetToken.DoesNotExist:
            return Response({
                "valid": False,
                "message": "Token invalide ou expiré"
            }, status=status.HTTP_400_BAD_REQUEST)
    
class PasswordResetConfirmView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        if not token or not new_password:
            return Response(
                {'error': 'Token et nouveau mot de passe requis.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            reset_token = PasswordResetToken.objects.get(
                token=token,
                expires_at__gt=timezone.now()  # Vérifie que le token n'a pas expiré
            )
        except PasswordResetToken.DoesNotExist:
            return Response(
                {'error': 'Lien invalide ou expiré.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Mettre à jour le mot de passe
        user = reset_token.user
        user.password = make_password(new_password)  # Hash le mot de passe
        user.save()

        # Supprimer le token utilisé (empêche la réutilisation)
        reset_token.delete()

        return Response(
            {'message': 'Mot de passe réinitialisé avec succès.'},
            status=status.HTTP_200_OK
        )