from django.shortcuts import render, HttpResponse
from .models import Company
from .serializer import CompanySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index (request):
    return HttpResponse("Pages d'entreprises")

class CompaniesList(APIView):

    def get(self, request, format = None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        """
        Create a new company
        """
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)