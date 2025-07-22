from django.db import models
from django.contrib.auth.models import User
import uuid 
from django.utils import timezone

class CustomerProfile(models.Model):
    # Le lien One-to-One vers le modèle User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                        related_name='account_customer_profile')

    # Champs spécifiques aux clients
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profil Client de {self.user.username}"

class FirmProfile(models.Model):
    # Le lien One-to-One vers le modèle User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='firm_profile')

    # Champs spécifiques aux entreprises
    company_name = models.CharField(max_length=255)
    siret = models.CharField(max_length=14, unique=True)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Profil Entreprise de {self.user.username}"
    
class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return self.expires_at > timezone.now()

    def __str__(self):
        return f"Token for {self.user.username}"