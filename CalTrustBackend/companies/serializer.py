# serializers.py
from rest_framework import serializers
from .models import Company
from account.models import FirmProfile

class FirmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmProfile
        fields = ['company_name', 'address']  # Champs à exposer

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
    # On ajoute le serializer de FirmProfile pour bien gérer l'objet imbriqué
    name = FirmProfileSerializer(read_only=True)

    # On ajoute ces propriétés en lecture seule, car elles sont calculées
    review_count = serializers.IntegerField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'category',
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

