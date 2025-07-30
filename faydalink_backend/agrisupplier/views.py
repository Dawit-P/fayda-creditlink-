from django.shortcuts import render
from rest_framework import viewsets
from .models import SupplyRequest
from .serializers import SupplyRequestSerializer

# Create your views here.

class SupplyRequestViewSet(viewsets.ModelViewSet):
    queryset = SupplyRequest.objects.all()
    serializer_class = SupplyRequestSerializer
