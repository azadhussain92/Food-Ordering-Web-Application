from django.urls import path
from menu import views


urlpatterns = [
    path('menu-dashboard', views.dashboard, name='menu_dashboard'),
    path('food_menu/',views.foodmenu,name='foodmenu'),
    path('food_edit/<int:pk>/', views.food_edit, name='food_edit'),
    path('food_delete/<int:pk>/', views.food_delete, name='food_delete'),
]