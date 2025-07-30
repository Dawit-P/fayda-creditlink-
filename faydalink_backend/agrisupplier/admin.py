from django.contrib import admin
from .models import Farmer, SupplyItem, SupplyRequest

admin.site.register(Farmer)
admin.site.register(SupplyItem)
admin.site.register(SupplyRequest)
