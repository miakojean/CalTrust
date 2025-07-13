from django.urls import path 
from .views import *

urlpatterns = [
    path("", CompaniesList.as_view(), name ="companies")
]