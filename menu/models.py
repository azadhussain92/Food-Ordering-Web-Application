from django.db import models
from accounts.models import VendorDetails



# Create your models here.
class FoodItems(models.Model):

    Categories=[('BREAKFAST','Breakfast'),
                ('LUNCH','Lunch'),
                ('DINER','Diner'),
                ('BRAVERAGES','Braverages'),
                ('DESSARTS','Dessarts'),
                ]

    vendor = models.ForeignKey(VendorDetails, on_delete=models.CASCADE, null=True, blank=True)
    name =models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='foodimage/',blank=True,null=True)
    Categery=models.CharField(max_length=10,choices=Categories)
    is_available = models.BooleanField(default=True)



