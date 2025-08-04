from django.urls import path 
from .views import *

urlpatterns = [
    path("", MyFirmsUser.as_view(), name="firms"),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('search/', CompanySearchView.as_view(), name='company-search'),
]