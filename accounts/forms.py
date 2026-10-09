from django import forms
from django.contrib.auth.models import User
from accounts.models import UserDetails,VendorDetails
from django_recaptcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        # field = "__all__"
        fields = ['username','email','password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserDetails
        fields= ['phone',
                 'house_no',
                 'address',
                 'city',
                 'state',
                 'zipcode',
                 'userpic'
                ]
    captcha=ReCaptchaField()

class UserUpdateFrom(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','email']


class UserUpdateDetailsFrom(forms.ModelForm):
    class Meta:
        model= UserDetails
        fields=['phone','house_no','address','city','state','zipcode','userpic']
    

#vendor regestratraion
class Vendorfrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']


class VendorProfileForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model=VendorDetails
        fields=['RestruntName',
                'lic_no',
                'Gst_no',
                'lic_certificate',
                'res_email',
                'res_phone',
                'res_address',
                'landmark',
                'zipcode',
                'res_image',
                ] 
      


