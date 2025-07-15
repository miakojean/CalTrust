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
    authentication_classes = [] # No authentication required
    permission_classes = [AllowAny] # Allow any user (authenticated or not) to access
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user_profile = serializer.save() 
            
            response_data = {
                "message": "User and profile created successfully!",
                "username": user_profile.user.username,
                "email": user_profile.user.email,
                "user_type": "customer" if isinstance(user_profile, CustomerProfile) else "firm"
            }
            
            # Add company details to response if it's a firm
            if isinstance(user_profile, FirmProfile) and user_profile.company:
                response_data["company_details"] = {
                    "name": user_profile.company.name,
                    "category": user_profile.company.category,
                    "siret": user_profile.company.siret,
                    "address": user_profile.company.address
                }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)