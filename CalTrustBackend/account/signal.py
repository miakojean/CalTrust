# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, CustomerProfile, FirmProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Crée automatiquement le profil correspondant lors de la création d'un utilisateur"""
    if created:
        if instance.user_type == 'CUSTOMER':
            CustomerProfile.objects.create(user=instance)
        elif instance.user_type == 'FIRM':
            FirmProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Sauvegarde automatiquement le profil quand l'utilisateur est sauvegardé"""
    if hasattr(instance, 'customer_profile'):
        instance.customer_profile.save()
    elif hasattr(instance, 'firm_profile'):
        instance.firm_profile.save()