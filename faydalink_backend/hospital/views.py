from django.shortcuts import render
from rest_framework import viewsets
from .models import PatientRequest
from .serializers import PatientRequestSerializer

# Create your views here.

class PatientRequestViewSet(viewsets.ModelViewSet):
    queryset = PatientRequest.objects.all()
    serializer_class = PatientRequestSerializer
