from django.urls import path 
from .views import *

urlpatterns = [
    path("", MyFimrsUser.as_view(), name="firms")
]