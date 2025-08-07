# serializers.py
from rest_framework import serializers
from .models import Company
from account.models import FirmProfile

#On définit le serialiser de FirmProfile puisqu'ils sont liés
class FirmProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    
    class Meta:
        model = FirmProfile
        fields = ['user_id', 'company_name', 'address']
        read_only_fields = ['user_id', 'company_name', 'address']

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
    # Le serializer imbriqué utilisera maintenant user_id au lieu de id
    name = FirmProfileSerializer(read_only=True)
    
    # Pour avoir directement l'ID du FirmProfile (user_id) au niveau racine
    firm_profile_id = serializers.PrimaryKeyRelatedField(
        source='name.user', 
        read_only=True
    )
    category_display = serializers.CharField(
        source='get_category_display', 
        read_only=True
    )
    
    review_count = serializers.IntegerField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'firm_profile_id',  # Donne direct l'ID du FirmProfile
            'category',
            'category_display',
            'description',
            'website',
            'review_count',
            'average_rating',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

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

