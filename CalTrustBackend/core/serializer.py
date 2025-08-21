from rest_framework import serializers
from .models import Notifications
from account.models import FirmProfile, CustomerProfile
from reviews.models import Review

class NotificationsSerializer(serializers.ModelSerializer):

    firm_name = serializers.CharField(source = 'firm.user.company_name')
    customer = serializers.CharField(source = 'customer.user.username')
    review = serializers.CharField(source = 'review')

    class Meta:
        model = Notifications
        fields = [
            'id',
            'firm_name',
            'customer',
            'review',
            'notifications_type',
            'message',
            'data',
            'is_read',
            'created_at',
            'target_url'
        ]