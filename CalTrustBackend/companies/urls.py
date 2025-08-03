from django.urls import path 
from .views import *

urlpatterns = [
    path("", MyFimrsUser.as_view(), name="firms"),
    path('/category/<str:category_code>/', CompanyByCategory.as_view(), name='firms-by-category')
]