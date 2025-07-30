from django.db import models

class Farmer(models.Model):
    full_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class SupplyItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class SupplyRequest(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    item = models.ForeignKey(SupplyItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.item.price * self.quantity
        super().save(*args, **kwargs)
