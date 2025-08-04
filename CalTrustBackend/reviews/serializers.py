from .models import *
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    firm_name = serializers.CharField(source='firm.company_name', read_only=True)
    customer_name = serializers.CharField(source='customer.user.username', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'firm_name', 'customer_name', 
                'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'firm', 'customer', 'created_at']
        extra_kwargs = {
            'rating': {
                'required': True,
                'min_value': 1,
                'max_value': 5
            },
            'comment': {
                'required': True,
                'min_length': 10
            }
        }

class PublicReviewSerializer(serializers.ModelSerializer):
    establishment = serializers.CharField(source='firm.company_name')
    user = serializers.CharField(source = 'customer.user.username')
    user_initial = serializers.SerializerMethodField()
    rating_stars = serializers.SerializerMethodField()
    local_date = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'id', 'establishment', 'rating', 'rating_stars',
            'comment', 'local_date', 'user_initial', 'user',
        ]
        read_only_fields = fields

    def get_username(self, obj):
        return obj.customer.user.username

    def get_user_initial(self, obj):
        # Protection vie privée : seul l'initiale est visible
        return obj.customer.user.username[0].upper() + "."
    
    def get_rating_stars(self, obj):
        return "★" * obj.rating + "☆" * (5 - obj.rating)
    
    def get_local_date(self, obj):
        # Format jour/mois français
        return obj.created_at.strftime("%d/%m à %Hh%M")
    
class ReviewResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewResponse
        fields = [
            'id',
            'review',
            'firm',
            'response_text',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']