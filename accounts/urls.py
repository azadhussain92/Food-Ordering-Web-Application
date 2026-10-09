from django.urls import path
from accounts import views




urlpatterns = [ 
    path('',views.regestation,name='regester'),
    path('login',views.loginpage,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('home/',views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('VendorProfile/', views.VendorProfile, name='VendorProfile'),
    path('update/', views.update, name='update'),
    path('vendor-register/', views.vendor_register, name='vendor_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('food-menu/', views.foodmenu, name='foodmenu'),
    path('approved', views.approved, name='approved'),
    path('Rest/<int:id>/', views.Rest_details, name='Rest'),
    path('add-to-card/<int:id>/', views.add_to_card, name='add_to_card'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),   
    

]