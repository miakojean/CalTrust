from rest_framework import serializers
from .models import Notification

class NotificationsSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    customer_username = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'firm',
            'customer',
            'customer_username',
            'review',
            'comment',
            'rating',
            'notifications_type',
            'message',
            'data',
            'is_read',
            'created_at',
            'target_url'
        ]

    def get_rating(self, obj):
        return obj.review.rating if obj.review else None

    def get_comment(self, obj):  # Corrigé le nom de la méthode
        return obj.review.comment if obj.review else None

    def get_customer_username(self, obj):
        return obj.customer.user.username if obj.customer and obj.customer.user else None