from django.contrib.auth import get_user_model
from .models import Notifications

User = get_user_model()

class NotificationService:

    @staticmethod
    def create_notification(firm,
                            customer, 
                            notification_type, 
                            message, data=None, 
                            target_url=None):
        """Crée une notification pour un utilisateur"""
        notification = Notifications.objects.create(
            firm = firm,
            customer = customer,
            notifications_type=notification_type,  # Correction du nom du champ
            message=message,
            data=data or {},
            target_url=target_url
        )
        return notification
    
    @staticmethod
    def mark_as_read(notification_id, user):
        """Marque une notification comme lue"""
        try:
            notification = Notifications.objects.get(id=notification_id, user=user)
            notification.is_read = True
            notification.save()
            return True
        except Notifications.DoesNotExist:
            return False
    
    @staticmethod
    def mark_all_as_read(user):
        """Marque toutes les notifications non lues d'un utilisateur comme lues"""
        Notifications.objects.filter(user=user, is_read=False).update(is_read=True)

    @staticmethod
    def get_unread_count(user):
        """Retourne le nombre de notifications non lues pour un utilisateur"""
        # CORRECTION: Utiliser Notifications au lieu de Notification
        return Notifications.objects.filter(user=user, is_read=False).count()
    
    @staticmethod
    def get_user_notifications(user, limit=20):
        """Retourne les notifications d'un utilisateur"""
        # CORRECTION: Utiliser Notifications au lieu de Notification
        return Notifications.objects.filter(user=user).order_by('-created_at')[:limit]