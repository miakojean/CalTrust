from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
    
    # Optionnel: Si vous voulez inclure les statistiques des avis
    review_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()