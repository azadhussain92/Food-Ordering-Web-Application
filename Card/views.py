# from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import CardItem,FoodItems

# Create your views here.

# @login_required
# def add_to_card(request):

#     card_items = CardItem.objects.filter(user=request.user)
#     total = sum(item.food_item.price * item.quantity for item in card_items )

#     return render(request, 'accounts/card.html', {'card_items': card_items,'total': total, })
