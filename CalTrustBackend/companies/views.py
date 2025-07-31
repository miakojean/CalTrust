from django.shortcuts import render, HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from account.models import FirmProfile
from rest_framework.permissions import AllowAny

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