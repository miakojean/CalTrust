from django.contrib.auth.models import User
from rest_framework import serializers
from .models import My_User

class MyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', write_only=True)
    email = serializers.EmailField(source='user.email', write_only=True)
    password = serializers.CharField(source='user.password', write_only=True, style={'input_type': 'password'})

    class Meta:
        model = My_User
        fields = ['id', 'user_type', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extraction des données du User
        user_data = validated_data.pop('user')
        
        # Création du User
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        
        # Création du My_User lié
        my_user = My_User.objects.create(
            user=user,
            user_type=validated_data['user_type']
        )
        
        return my_user