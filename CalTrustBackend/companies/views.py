from django.shortcuts import render, HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index (request):
    return HttpResponse("Pages d'entreprises")

