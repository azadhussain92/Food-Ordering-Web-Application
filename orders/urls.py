from django.urls import path
from orders import views


urlpatterns = [
    path('', views.order_details, name='order_details'),
    
]