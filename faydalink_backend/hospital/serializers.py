from rest_framework import serializers
from .models import Patient, MedicalService, PatientRequest

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = '__all__'

class PatientRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRequest
        fields = '__all__'
