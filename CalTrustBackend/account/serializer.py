# your_app_name/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomerProfile, FirmProfile # Make sure to import FirmProfile
from companies.models import Company

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    user_type = serializers.ChoiceField(choices=['customer', 'firm'])

    # Customer-specific fields (optional)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    birth_date = serializers.DateField(required=False, allow_null=True)

    # Company-specific fields (required if user_type is 'firm')
    company_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    company_category = serializers.ChoiceField(choices=Company.CATEGORY, required=False)
    company_description = serializers.CharField(required=False, allow_blank=True)
    company_siret = serializers.CharField(max_length=14, required=False, allow_blank=True)
    company_address = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        # Custom validation to ensure company fields are provided for 'firm' users
        if data.get('user_type') == 'firm':
            if not data.get('company_name'):
                raise serializers.ValidationError({"company_name": "Company name is required for firm registration."})
            if not data.get('company_category'):
                raise serializers.ValidationError({"company_category": "Company category is required for firm registration."})
            # siret and address can be optional for company too, depending on your business rules
        return data

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        # Create the Django User
        user = User.objects.create_user(username=username, email=email, password=password)

        if user_type == 'customer':
            customer_profile_data = {
                'phone': validated_data.get('phone', ''),
                'birth_date': validated_data.get('birth_date', None)
            }
            profile = CustomerProfile.objects.create(user=user, **customer_profile_data)
        
        elif user_type == 'firm':
            # Extract company data
            company_data = {
                'name': validated_data.pop('company_name'),
                'category': validated_data.pop('company_category'),
                'description': validated_data.pop('company_description', ''),
                'siret': validated_data.pop('company_siret', None),
                'address': validated_data.pop('company_address', '')
            }
            
            # Create the Company instance
            company = Company.objects.create(**company_data)

            # Create the FirmProfile and link it to the Company
            profile = FirmProfile.objects.create(user=user, company=company)
        
        else:
            raise serializers.ValidationError("Invalid user_type provided.")
        
        return profile

    def update(self, instance, validated_data):
        # Update logic is complex for this type of serializer (User + varied Profile + Company)
        # For a registration endpoint, 'create' is usually the main focus.
        pass