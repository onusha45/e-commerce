from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import login ,logout,authenticate 
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from category.models import *
# Create your views here.
def singleproduct(request, pid):  
    product = AddProduct.objects.get(id=pid)
    return render(request, 'singleproduct.html', {'product': product})
def products(request):
   items = AddProduct.objects.all()  # Fetch items from your database
   context = {'items': items}
   return render(request, 'products.html', context)
def productform(request):
   return render(request,"productform.html")
@user_passes_test(lambda u: u.is_superuser)
@login_required
def adminindex(request):
    data ={
        'dashboard_active_page':'active'
    }
    return render(request, 'Admin/index.html',data)
def adminlogin(request):
    data ={
        'login_active_page':'active'
    }
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:  # Check if the user is an admin/staff
                login(request, user)
                return redirect('adminindex')  # Redirect to admin index/dashboard
            else:
                error_message = 'You are not authorized to access this page.'
        else:
            error_message = 'Invalid username or password.'

    return render(request, 'Admin/login.html',data)
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')
def admineditproduct(request):

    return render(request, 'Admin/edit-product.html')
@login_required
def adminproduct(request):
    data ={
        'product_active_page':'active',
        'Product_item':AddProduct.objects.all(),
        'Product_cat':Category.objects.all()
    }
   

    return render(request, 'Admin/products.html',data)

def adminaccount(request):
    data ={
        'account_active_page':'active'
    }
    return render(request, 'Admin/accounts.html',data)

def adminaddproduct(request):
    categories = Category.objects.all()
    return render(request, 'Admin/addproduct.html', {'categories': categories})

def adminaddcategory(request):
   
    return render(request, 'Admin/category.html')
def adminsavecategory(request):
        print(request.POST.items)
        cat_name = request.POST['cat_name']
        
        Saveadmincategory = Category(
           name =cat_name   
        )
        Saveadmincategory.save()
        
        print(f"Received form data - Category_name: {cat_name}")
        
        return redirect("adminproduct")
def adminsaveproduct(request):
        print(request.POST.items)
        name = request.POST['name']
        description = request.POST['description']
        expire_date = request.POST['expire_date']
        stock = request.POST['stock']
        price = request.POST['price']
        product_image = request.FILES['product_image']
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        
        Saveadminproduct = AddProduct(
            Product_name=name,
            Description=description,
            Expiry_Date=expire_date,
            Stock_unit=stock,
            Product_img=product_image,
            Product_price =price,
            category = category,
        )
        Saveadminproduct.save()
        
        print(f"Received form data - Product_name: {name}, Description: {description}, Expiry_date: {expire_date}, Stock_unit: {stock}")
        
        return redirect("adminproduct")
    
def delete_product(request,pid):
    product = AddProduct.objects.get(id=pid)
    product.delete()
    return redirect('adminproduct')
def delete_category(request,pid):
    product = Category.objects.get(id=pid)
    product.delete()
    return redirect('adminproduct')