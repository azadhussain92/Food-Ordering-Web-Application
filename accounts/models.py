from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional field
    phone= models.BigIntegerField()
    house_no = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    zipcode= models.IntegerField()
    userpic= models.ImageField(upload_to='userpic/',blank=True,null=True)

    
    def __str__(self):
        return self.user.username
    




#  create a vendor fieldss
class VendorDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
#additional details
    RestruntName = models.CharField(max_length=100)
    lic_no= models.CharField(max_length=100)
    Gst_no=models.CharField(max_length=100)
    res_email= models.EmailField()
    res_phone= models.BigIntegerField()
    res_address=models.TextField()
    landmark=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    lic_certificate= models.ImageField(upload_to='liccer/',blank=True,null=True)
    res_image=models.ImageField(upload_to='resimg/',blank=True,null=True)
    is_approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.RestruntName 