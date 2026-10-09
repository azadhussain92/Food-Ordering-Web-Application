from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItems
from accounts.models import VendorDetails


# Create your models here.
class CardItem(models.Model):

    Categories=[('BREAKFAST','Breakfast'),
                ('LUNCH','Lunch'),
                ('DINER','Diner'),
                ('BRAVERAGES','Braverages'),
                ('DESSARTS','Dessarts'),
                ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name =models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='foodimage/',blank=True,null=True)
    Categery=models.CharField(max_length=10,choices=Categories)
    vendor = models.ForeignKey(VendorDetails,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def total_items(self):
        return self.price * self.quantity



