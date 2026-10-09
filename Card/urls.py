from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_to_card, name='add_to_card'),
    # path('cart/', views.cart_view, name='cart'),
    
]