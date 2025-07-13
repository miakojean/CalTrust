from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import MyUserSerializer
from .models import My_User
# Create your views here.
def index (request):
    return HttpResponse("Bienvenu au pays ")

class UserRegistration(APIView):

    def get(self, request, format = None):
        user = My_User.objects.all()
        serializer = MyUserSerializer(user, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Create a new user with profile
        """
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'id': serializer.data['id'],
                'user_type': serializer.data['user_type'],
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)