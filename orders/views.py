from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from orders.models import allorders,OrderItem
from Card.models import CardItem
from django.utils import timezone


# Create your views here.

# def order_details(request):
#     order =allorders.objects.create()
#     order.save()
#     # print(order.orderid)
#     print("ORDER ID =", order.orderid)
#     return render(request,'accounts/orders.html',{'orderid': order.orderid})

@login_required
def order_details(request):
    #current user in the cart items
    cart_items = CardItem.objects.filter(user=request.user)
    # if cart empty
    if not cart_items.exists():
        return redirect('home')
    #subtotal
    subtotal = Decimal('0.00')
    for items in cart_items:
        subtotal += (items.price * items.quantity)
     # Platform Fee
    Platform_Fee = Decimal('20.00')
    
    #GST
    cgst = subtotal * Decimal('0.025')
    sgst = subtotal * Decimal('0.025')

    #grand total
    grand_total = (subtotal + Platform_Fee + cgst + sgst)

    now = timezone.localtime()
    order = allorders.objects.create(user=request.user,subtotal=subtotal,Platform_Fee=Platform_Fee,cgst=cgst,sgst=sgst,grand_total=grand_total,order_date=now.date(),order_time=now.time())

    #cart item copy on orderitems
    for item in cart_items:
        amount =(item.price * item.quantity)
        OrderItem.objects.create(
                                order=order,
                                name=item.name,
                                price=item.price,
                                quantity=item.quantity,
                                amount=amount,
                                vendor=item.vendor
                            )

    #if order is plased then cart empty
    cart_items.delete()
    print("ORDER ID :-" , order.orderid)
    return render(request, 'accounts/orders.html',{'order': order,'orderid': order.orderid })