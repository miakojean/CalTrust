from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class My_User(models.Model):
    USER_TYPE = [
        ("CUSTOMER", "CUSTOMER"),
        ("FIRMS", "FIRMS")
    ]
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, blank=False)

    def __str__(self):
        return f'utilisateur de type {self.user_type}'
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class FirmProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='firm_profile')
    company_name = models.CharField(max_length=255)
    siret = models.CharField(max_length=14, unique=True)
    address = models.TextField()