from django.urls import path 
from .views import *

urlpatterns = [
    path("", LatestCompanies.as_view(), name="firms"),
    path('<int:id>/', CompanyDetail.as_view()),
    path('my-company/', MyCompanyUserAccount.as_view(), name='my-company'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('search/', CompanySearchView.as_view(), name='company-search'),
]