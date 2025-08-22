from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class NotificationService:

    @staticmethod
    def create_notification(firm,
                            customer, 
                            notification_type,
                            review, 
                            message, data=None, 
                            target_url=None):
        """Crée une notification pour un utilisateur"""
        notification = Notification.objects.create(
            firm = firm,
            customer = customer,
            review = review,
            notifications_type=notification_type,  # Correction du nom du champ
            message=message,
            data=data or {},
            target_url=target_url
        )
        return notification
    
    @staticmethod
    def mark_as_read(notification_id, firm):
        """Marque une notification comme lue"""
        try:
            notification = Notification.objects.get(id=notification_id, firm = firm)
            notification.is_read = True
            notification.save()
            return True
        except Notification.DoesNotExist:
            return False
    
    @staticmethod
    def mark_all_as_read(firm):
        """Marque toutes les notifications non lues d'un utilisateur comme lues"""
        Notification.objects.filter(firm = firm, is_read=False).update(is_read=True)

    @staticmethod
    def get_unread_count(firm):
        """Retourne le nombre de notifications non lues pour un utilisateur"""
        # CORRECTION: Utiliser Notifications au lieu de Notification
        return Notification.objects.filter(firm = firm, is_read=False).count()
    
    @staticmethod
    def get_user_notifications(firm, limit=20):
        """Retourne les notifications d'un utilisateur"""
        # CORRECTION: Utiliser Notifications au lieu de Notification
        return Notification.objects.filter(firm = firm).order_by('-created_at')[:limit]