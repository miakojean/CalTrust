from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Remplace le username par l'email comme identifiant
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Retire 'email' car c'est déjà USERNAME_FIELD

    # Types d'utilisateurs
    class UserType(models.TextChoices):
        CLIENT = 'C', 'Client'
        BUSINESS = 'B', 'Business'

    email = models.EmailField(unique=True)  # Email obligatoire et unique
    username = None  # Désactive le champ username
    user_type = models.CharField(
        max_length=1,
        choices=UserType.choices,
        default=UserType.CLIENT
    )

    def __str__(self):
        return self.email

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # Autres champs clients...

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    company_name = models.CharField(max_length=255)
    siret = models.CharField(max_length=14, unique=True)  # Exemple pour la France
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)
    # Autres champs entreprises...

AUTH_USER_MODEL = 'users.User'  # Indique à Django d'utiliser votre modèle custom