from django.urls import path
from .views import *

urlpatterns = [
    path('', UserRegistration.as_view(), name='index'),
]