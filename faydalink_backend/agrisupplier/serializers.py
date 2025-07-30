from rest_framework import serializers
from .models import Farmer, SupplyItem, SupplyRequest

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class SupplyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyItem
        fields = '__all__'

class SupplyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyRequest
        fields = '__all__'
