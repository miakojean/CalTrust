from django.db import models
from django.contrib.auth.models import User
import uuid 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image  # Import de Pillow
import os
from django.conf import settings


class CustomerProfile(models.Model):
    # Le lien One-to-One vers le modèle User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                        related_name='account_customer_profile')

    # Champs spécifiques aux clients
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    # Photo de profil
    profile_picture = models.ImageField(
        upload_to='profile_pictures/customers/',
        null=True,
        blank=True,
        verbose_name=_("Photo de profil")
    )

    def __str__(self):
        return f"Profil Client de {self.user.username}"
    
    def save(self, *args, **kwargs):
        # Appeler d'abord la méthode save originale
        super().save(*args, **kwargs)
        
        # Redimensionner l'image si elle existe
        if self.profile_picture:
            self.resize_image(self.profile_picture.path, (300, 300))

    @staticmethod
    def resize_image(image_path, size):
        """Redimensionne l'image à la taille spécifiée"""
        try:
            with Image.open(image_path) as img:
                # Convertir en RGB si nécessaire
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Redimensionner en conservant le ratio
                img.thumbnail(size, Image.Resampling.LANCZOS)
                img.save(image_path, optimize=True, quality=85)
        except Exception as e:
            # Gérer les erreurs silencieusement ou logger l'erreur
            print(f"Erreur lors du redimensionnement de l'image: {e}")

    def delete(self, *args, **kwargs):
        """Supprime l'image du système de fichiers lors de la suppression du profil"""
        if self.profile_picture:
            # Supprimer le fichier image
            if os.path.isfile(self.profile_picture.path):
                os.remove(self.profile_picture.path)
        super().delete(*args, **kwargs)


class FirmProfile(models.Model):
    # Le lien One-to-One vers le modèle User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                primary_key=True, 
                                related_name='firm_profile')

    # Champs spécifiques aux entreprises
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Numéro de téléphone"))
    
    # Logo de l'entreprise
    company_logo = models.ImageField(
        upload_to='profile_pictures/firms/',
        null=True,
        blank=True,
        verbose_name=_("Logo de l'entreprise")
    )

    def __str__(self):
        return f"Profil Entreprise de {self.user.username}"
    
    def save(self, *args, **kwargs):
        # Appeler d'abord la méthode save originale
        super().save(*args, **kwargs)
        
        # Redimensionner les images si elles existent
        if self.company_logo:
            self.resize_image(self.company_logo.path, (300, 300))
        

    @staticmethod
    def resize_image(image_path, size):
        """Redimensionne l'image à la taille spécifiée"""
        try:
            with Image.open(image_path) as img:
                # Convertir en RGB si nécessaire
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Redimensionner en conservant le ratio
                img.thumbnail(size, Image.Resampling.LANCZOS)
                img.save(image_path, optimize=True, quality=85)
        except Exception as e:
            # Gérer les erreurs silencieusement ou logger l'erreur
            print(f"Erreur lors du redimensionnement de l'image: {e}")

    def delete(self, *args, **kwargs):
        """Supprime les images du système de fichiers lors de la suppression du profil"""
        # Supprimer le logo
        if self.company_logo:
            if os.path.isfile(self.company_logo.path):
                os.remove(self.company_logo.path)
                
        super().delete(*args, **kwargs)


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return self.expires_at > timezone.now()

    def __str__(self):
        return f"Token for {self.user.username}"