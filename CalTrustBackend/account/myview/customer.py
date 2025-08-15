from ..models import Company
from ..serializer import CompanySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CompaniesList(APIView):
    def get(self, request, format = None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many = True)
        return Response(serializer.data)