from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    CATEGORY = [
        ("Commerce", "Commerce"),
        ("Alimentation", "Alimentation"),
        ("Immobilier", "Immobilier")
    ]
    name = models.CharField(max_length=100, blank=False, unique=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'entreprise {self.name}'
    
class CustomerProfile(models.Model):
    # One-to-One link to Django's User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, 
                              related_name='company_customer_profile')

    def __str__(self):
        return f"Profil Client de {self.user.username}"

class FirmProfile(models.Model):
    # One-to-One link to Django's User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='company_firm_profile')
    
    # Foreign Key to the Company model.
    # A firm user (FirmProfile) belongs to one company.
    # A company can have many firm users (FirmProfiles).
    # SET_NULL allows the FirmProfile to remain if the Company is deleted (company field becomes null).
    # null=True, blank=True allows a FirmProfile to be created without an immediate company link,
    # though for registration, we'll ensure it's linked.
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='firm_users')

    def __str__(self):
        company_name = self.company.name if self.company else "No Company"
        return f"Profil Entreprise de {self.user.username} (associé à {company_name})"