from django.contrib import admin
from .models import Patient, MedicalService, PatientRequest

admin.site.register(Patient)
admin.site.register(MedicalService)
admin.site.register(PatientRequest)
