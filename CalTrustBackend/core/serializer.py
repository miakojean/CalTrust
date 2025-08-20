from rest_framework import serializers
from .models import Notifications
from account.models import FirmProfile, CustomerProfile
from reviews.models import Review

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'