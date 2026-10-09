from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from accounts.forms import UserForm,UserProfileForm,UserUpdateFrom,Vendorfrom,VendorProfileForm,VendorDetails
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import UserDetails,VendorDetails
from menu.models import FoodItems
from Card.models import CardItem
from django.contrib import messages
from decimal import Decimal


# Create your views here.

def regestation(request):
    regester=False
    if request.method == 'POST':
            froms1 = UserForm(request.POST)
            froms2 = UserProfileForm(request.POST,request.FILES)

            print('FILES:',request.FILES)
            print('USERPIC:',request.FILES.get("userpic"))

            if froms1.is_valid() and froms2.is_valid():
                  user = froms1.save()
                  user.set_password(user.password)
                  user.save()

                  profile = froms2.save(commit=False)
                  profile.user = user
                  profile.userpic = request.FILES.get("userpic")
                  profile.save()
                  print('SAVED IMAGE=',profile.userpic)
                  regester = True
           
    else:
            froms1 = UserForm()
            froms2 = UserProfileForm()
    context= {
            'froms1': froms1,
            'froms2': froms2,
            'regester':regester
            }
    return render(request, "accounts/regestation.html",context)

# def loginpage(request):
#       if request.method == 'POST':
#             username= request.POST.get('username')
#             password= request.POST.get('password')
#             print(username)
#             print(password)

#             user = authenticate(username=username,password=password)

#             if user is not None:
#                   if user.is_active:
#                         login(request, user)
#                         return redirect('home')
#                   else:
#                         return HttpResponse('user is not active')
#             else:
#                   return HttpResponse("no user founds")
              
#       return render(request,'accounts/login.html')




@login_required(login_url='login')
def home(request):
    #   phon = UserDetails.objects.values('phone')
        # return render(request, 'home.html',{})
        vendors = VendorDetails.objects.filter(is_approved=True)
        return render(request, 'home.html', {'vendors': vendors})

@login_required(login_url='login')
def  user_logout(request):
      logout(request)
      return redirect("login")

# show the restruant details
def Rest_details(request, id=0):
    info = get_object_or_404(VendorDetails, id=id)
    food_items = FoodItems.objects.filter(vendor=info)
    return render(request, 'accounts/Rest_details.html', {'info': info, 'food_items': food_items})


@login_required(login_url='login')
def profile(request):

    vendor = VendorDetails.objects.filter(user=request.user).first()

    if vendor:
        return render(request,'accounts/VendorProfile.html',{'vendor':vendor})
    details = get_object_or_404(UserDetails,user=request.user)

    return render(request,'accounts/profile.html',{'details': details})

#vendorprofile
@login_required(login_url='login')
def VendorProfile(request):
    vendor = get_object_or_404(VendorDetails, user=request.user)
    return render(
        request,
        'accounts/VendorProfile.html',
        {'vendor': vendor}
    )


@login_required(login_url='login')
def update(request):
      if request.method =='POST':
            form= UserUpdateFrom(request.POST,instance=request.user)
            froms1 = UserProfileForm(request.POST,request.FILES,instance=request.user.userdetails)

            if form.is_valid() and froms1.is_valid():
                  form.save()
                  froms1.save()
                  profile = froms1.save(commit=False)
                  profile.user = request.user
                  profile.save()
                  return redirect('profile')
      else:
            form=UserUpdateFrom(instance=request.user)
            froms1 = UserProfileForm(instance=request.user.userdetails)

      return render(request,'accounts/update.html',{'form':form,'froms1':froms1})


# vendor details
def vendor_register(request):
     regester=False
     if request.method=='POST':
      
            form= Vendorfrom(request.POST)
            form2=VendorProfileForm(request.POST,request.FILES)
            if form.is_valid() and form2.is_valid():
                  # user =form.save()
                  user = form.save(commit=False)
                  user.set_password(user.password)
                  user.save() 
                  vendor =form2.save( commit=False)
                  vendor.user=user
                  vendor.save()
      
                  return render(request,'accounts/vendor.html',{'vendor_register':True})
     else:
          form=Vendorfrom()
          form2=VendorProfileForm()
     context = {
                  'form': form,
                  'form2': form2
    }
     return render(request,'accounts/vendor.html',context)

# dashboard 
@login_required(login_url='login')
def dashboard(request):
    vendor = VendorDetails.objects.get(user=request.user)
    food_items = FoodItems.objects.filter(vendor=vendor)
    print("Vendor ID:", vendor.id)          
    print("Django User ID:", request.user.id)
    context = {'vendor': vendor,'food_items': food_items}
    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
def foodmenu(request):
    return render(request, 'accounts/foodmenu.html')

@login_required(login_url='login')   
def approved(request):
      return redirect('food_menu')
      return render(request,'accounts/approved.html',{})


# login for both 
def loginpage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                # Check whether this user is a vendor
                vendor = VendorDetails.objects.filter(user=user).first()
                if vendor:
                    # Vendor exists, check admin approval
                    if vendor.is_approved:
                        login(request, user)
                        return redirect('dashboard')
                    else:
                        return HttpResponse('Please Wait For Admin Approval.')
                else:
                    # Normal User
                    login(request, user)
                    return redirect('home')
            else:
                return HttpResponse('User is not active')
        else:
            return HttpResponse('Invalid username or password')
    return render(request, 'accounts/login.html')



# show the card items 


# def add_to_card(request, id):
#     # if not request.user.is_authenticated:
#     #     return redirect('login')

#     food = get_object_or_404(FoodItems, id=id)

#     cart_item, created = CardItem.objects.get_or_create(
#         user=request.user,
#         name=food.name,
#         price=food.price,
#         vendor=str(food.vendor.id),
#         defaults={
#             'quantity': 1,
#             'Categery': food.Categery,
#             'image': food.image,
#         }
#     )

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('Rest', id=food.vendor.id)


def add_to_card(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    food = get_object_or_404(FoodItems, id=id)
    vendor = food.vendor

    cart_item = CardItem.objects.filter(
        user=request.user,
        name=food.name,
        price=food.price,
         vendor=vendor
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        CardItem.objects.create(
            user=request.user,
            name=food.name,
            price=food.price,
            image=food.image,
            Categery=food.Categery,
            vendor=vendor,
            quantity=1
        )

    return redirect('Rest', id=food.vendor.id)

# show the food in card

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CardItem.objects.filter(user=request.user)

    # Default values
    total = Decimal('0.00')
    Platform_Fee = Decimal('0.00')
    # Gst = Decimal('0.00')
    cgst = Decimal('0.00')
    sgst = Decimal('0.00')
    grand_total = Decimal('0.00')

    for item in cart_items:
        # item.total_items = item.price * item.quantity
        total += item.total_items

        #Platform Fee
        # Platform_Fee = 20
        Platform_Fee = Decimal('10.00')
        #Gst 5%
        # Gst = total * 5 /100
        # Gst = total * Decimal('0.05')
        cgst = total * Decimal('0.025')
        sgst = total * Decimal('0.025')

        #Grand total
        grand_total = total + Platform_Fee + cgst+sgst

    return render(request,'accounts/card.html',{'cart_items': cart_items,'total': total,'Platform_Fee':Platform_Fee,'cgst':cgst,'sgst':sgst,'grand_total':grand_total})


# increase_quantity and decrease_quantity

def increase_quantity(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    item = get_object_or_404(CardItem,id=id,user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')


def decrease_quantity(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    item = get_object_or_404(CardItem,id=id,user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart') 


#  count the item in cart   