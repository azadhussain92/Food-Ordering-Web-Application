from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from.forms import MenuForm
from .models import FoodItems
from accounts.models import VendorDetails

# Create your views here.

def foodmenu(request):
    vendor = VendorDetails.objects.filter(user=request.user).first()
    # if not vendor:
    #     return HttpResponse("Vendor profile not found for this user.")
    
    if request.method =='POST':
        form = MenuForm(request.POST,request.FILES)

        print('FILES:',request.FILES)
        print('foodimage:',request.FILES.get("foodimage"))

        if form.is_valid():
            food = form.save(commit=False)
            food.vendor = VendorDetails.objects.get(user=request.user)
            food.save()
            return redirect('dashboard')
    else:
        form = MenuForm()

    return render(request,'accounts/foodmenu.html',{'form':form})

def dashboard(request):
    # food_items = FoodItems.objects.all()
    vendor = get_object_or_404(VendorDetails, user=request.user)
    food_items = FoodItems.objects.filter(vendor=vendor)
    return render(request,'accounts/dashboard.html',{'food_items': food_items})


# food item edit and delate 

def food_edit(request, pk):
    food = get_object_or_404(FoodItems, pk=pk)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MenuForm(instance=food)
    return render(request, 'accounts/foodmenu.html', {'form': form})


def food_delete(request, pk):
    food = get_object_or_404(FoodItems, pk=pk)
    food.delete()
    return redirect('dashboard')