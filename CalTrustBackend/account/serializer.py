# your_app_name/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomerProfile, FirmProfile # Make sure to import FirmProfile
from companies.models import Company
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        error_messages={
            'required': 'Le nom d\'utilisateur est obligatoire',
            'max_length': 'Le nom d\'utilisateur ne doit pas dépasser 150 caractères'
        }
    )
    email = serializers.EmailField(
        error_messages={
            'required': 'L\'email est obligatoire',
            'invalid': 'Veuillez fournir une adresse email valide'
        }
    )
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        min_length=8,
        error_messages={
            'required': 'Le mot de passe est obligatoire',
            'min_length': 'Le mot de passe doit contenir au moins 8 caractères'
        }
    )
    
    user_type = serializers.ChoiceField(
        choices=['customer', 'firm'],
        error_messages={
            'required': 'Le type d\'utilisateur est obligatoire',
            'invalid_choice': 'Le type d\'utilisateur doit être "customer" ou "firm"'
        }
    )

    # Customer-specific fields
    phone = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
        error_messages={
            'max_length': 'Le numéro de téléphone ne doit pas dépasser 20 caractères'
        }
    )
    birth_date = serializers.DateField(
        required=False,
        allow_null=True,
        error_messages={
            'invalid': 'Veuillez fournir une date valide (format: AAAA-MM-JJ)'
        }
    )

    # Firm-specific fields
    company_name = serializers.CharField(
        max_length=255,
        required=False,
        allow_blank=True,
        error_messages={
            'max_length': 'Le nom de l\'entreprise ne doit pas dépasser 255 caractères'
        }
    )
    phone_number = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
        error_messages={
            'max_length': 'Le numéro de téléphone ne doit pas dépasser 20 caractères'
        }
    )
    address = serializers.CharField(
        required=False,
        allow_blank=True,
        error_messages={
            'invalid': 'Veuillez fournir une adresse valide'
        }
    )

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Veuillez fournir une adresse email valide")
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cette adresse email est déjà utilisée")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà pris")
        return value

    def validate_phone_number(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres")
        if value and len(value) != 10:
            raise serializers.ValidationError("Le numéro de téléphone doit contenir exactement 10 chiffres")
        return value

    def validate(self, data):
        if data.get('user_type') == 'firm':
            if not data.get('company_name'):
                raise serializers.ValidationError({
                    'company_name': 'Le nom de l\'entreprise est obligatoire pour les professionnels'
                })
            if not data.get('phone_number'):
                raise serializers.ValidationError({
                    'phone_number': 'Le numéro de téléphone est obligatoire pour les professionnels'
                })
            if not data.get('address'):
                raise serializers.ValidationError({
                    'address': 'L\'adresse est obligatoire pour les professionnels'
                })
        
        return data

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        user = User.objects.create_user(
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password')
        )

        if user_type == 'customer':
            profile = CustomerProfile.objects.create(
                user=user,
                phone=validated_data.get('phone', ''),
                birth_date=validated_data.get('birth_date')
            )
        else:
            profile = FirmProfile.objects.create(
                user=user,
                company_name=validated_data.get('company_name'),
                phone_number=validated_data.get('phone_number'),
                address=validated_data.get('address')
            )
        
        return profile

    def update(self, instance, validated_data):
        raise NotImplementedError("La mise à jour n'est pas implémentée pour ce sérialiseur")
    
# Ajoutez ceci à la fin du fichier serializer.py

class CustomerProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = CustomerProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'profile_picture']
        read_only_fields = ['username', 'email']

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            # Retourne l'URL complète de l'image
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # Mise à jour des champs utilisateur
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Mise à jour des champs du profil
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class CompanySerializer(serializers.ModelSerializer):
    firm_profile_id = serializers.PrimaryKeyRelatedField(source='name.user', read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    # Modifiez cette partie pour gérer plusieurs reviews

    class Meta:
        model = Company
        fields = [
            'id',
            'firm_profile_id',
            'category',
            'category_display',
            'description',
            'website',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class FirmProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    company = CompanySerializer(read_only = True)
    company_logo = serializers.ImageField(required=False, allow_null=True, )

    class Meta:
        model = FirmProfile
        fields = ['username', 
            'email', 
            'first_name', 
            'last_name', 
            'company_name', 
            'address', 
            'is_verified', 
            'phone_number',
            'company',
            'company_logo'
        ]
        read_only_fields = ['username', 'email', 'is_verified']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # Mise à jour des champs utilisateur
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Mise à jour des champs du profil
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance