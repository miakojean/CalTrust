# serializers.py
from rest_framework import serializers
from .models import Company
from account.models import FirmProfile
from reviews.models import Review

#On définit le serialiser de FirmProfile puisqu'ils sont liés
class FirmProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    
    class Meta:
        model = FirmProfile
        fields = ['user_id', 'company_name', 'address']
        read_only_fields = ['user_id', 'company_name', 'address']

# On va définir le serialiser de Review pour l'intégrer dans company quand on veut toutes les données!!!

class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.user.username', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id',
            'customer_name',
            'rating',
            'comment',
            'created_at',
            'updated_at',
            'response'  # Inclut la réponse de l'entreprise si elle existe
        ]
        depth = 1  # Pour inclure les données relationnelles

# Class to manage company as FimrUser

class CompanyAsUser(serializers.ModelSerializer):
    
    name = FirmProfileSerializer(read_only = True)
    
    class Meta:
        model = Company
        fields = [
            'name',
            'category', 
            'description',
            'website',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

#class to get company

class CompanySerializer(serializers.ModelSerializer):
    name = FirmProfileSerializer(read_only=True)
    firm_profile_id = serializers.PrimaryKeyRelatedField(source='name.user', read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    # Modifiez cette partie pour gérer plusieurs reviews
    reviews = serializers.SerializerMethodField()
    review_count = serializers.IntegerField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'firm_profile_id',
            'category',
            'category_display',
            'description',
            'website',
            'reviews',  # Renommé de 'review' à 'reviews' pour refléter qu'il y en a plusieurs
            'review_count',
            'average_rating',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_reviews(self, obj):
        # Récupère les 5 derniers avis triés par date
        reviews = obj.name.reviews.all().order_by('-created_at')[:5]
        return ReviewSerializer(reviews, many=True).data

class CompanySearchSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(
        source='get_category_display', 
        read_only=True
    )
    average_rating = serializers.FloatField(read_only=True)  # Suppression du source
    review_count = serializers.IntegerField(read_only=True)  # Idem ici
    name = serializers.StringRelatedField(source = 'name.user.username')

    class Meta:
        model = Company 
        fields = [
            'id',
            'name',
            'category',
            'category_display',
            'description',
            'website',
            'average_rating',  # Correspond à la propriété du modèle
            'review_count'     # Correspond à la propriété du modèle
        ]

