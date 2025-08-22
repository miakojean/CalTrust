from rest_framework import serializers
from .models import Notification

class NotificationsSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    customer_username = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'firm',
            'customer',
            'customer_username',
            'review',
            'rating',
            'notifications_type',
            'message',
            'data',
            'is_read',
            'created_at',
            'target_url'
        ]

    def get_rating(self, obj):
        # Récupérer la note depuis l'avis lié
        return obj.review.rating if obj.review else None

    def get_customer_username(self, obj):
        # Récupérer le nom d'utilisateur depuis le profil client
        return obj.customer.user.username if obj.customer and obj.customer.user else None