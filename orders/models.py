from django.db import models
from django.contrib.auth.models import User
import uuid
from menu.models import FoodItems
from accounts.models import VendorDetails

# Create your models here.
class allorders(models.Model):
    orderid = models.UUIDField(primary_key=True,default = uuid.uuid4,editable= False,unique= True,)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    order_date = models.DateField(null=True,blank=True)
    order_time = models.TimeField(null=True,blank=True)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    Platform_Fee = models.DecimalField( max_digits=10,decimal_places=2,default=0)
    cgst = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    sgst = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    grand_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    state = models.CharField(max_length=30,default='pending')

    def __str__(self):
        return str(self.orderid)

#order item detalis

class OrderItem(models.Model):

    order = models.ForeignKey(allorders,on_delete=models.CASCADE,related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    vendor = models.ForeignKey(VendorDetails,on_delete=models.CASCADE,null=True,blank=True
)

    def __str__(self):
        return self.name