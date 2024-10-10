from django.db import models
from django.utils import timezone

# Logistic Model
class Logistic(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Running Out', 'Running Out'),
        ('Out of Stock', 'Out of Stock'),
    ]

    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    stocked_date = models.DateField()
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def is_running_out(self):
        return self.quantity < 10  # Example threshold

    def update_status(self):
        if self.quantity == 0:
            self.status = 'Out of Stock'
        elif self.quantity < 10:  # Arbitrary threshold for "Running Out"
            self.status = 'Running Out'
        else:
            self.status = 'Available'
        self.save()

class Commodity(models.Model):
    CATEGORY_CHOICES = [
        ('chemicals', 'Chemicals'),
        ('equipment', 'Equipment'),
        ('consumables', 'Consumables'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)
    stocking_date = models.DateField()
    
    def __str__(self):
        return self.name

class StockHistory(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # e.g., "Added", "Deleted"
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.commodity.name} - {self.action} - {self.quantity} units"
