from .views import *
from django.urls import path

urlpatterns = [
    
     path('singleproduct/<int:pid>/', singleproduct , name='singleproduct'),
     path('products/', products , name='products'),
     path('productform/', productform , name='productform'),
     path('adminindex/', adminindex, name='adminindex'),
     path('adminlogin/', adminlogin, name='adminlogin'),
     path('adminlogout/', adminlogout, name='adminlogout'),
     path('adminproduct/', adminproduct, name='adminproduct'),
     path('adminaccount/', adminaccount, name='adminaccount'),
     path('adminaddproduct/', adminaddproduct, name='adminaddproduct'),
     path('adminaddcategory/', adminaddcategory, name='adminaddcategory'),
     path('admineditproduct/', admineditproduct, name='admineditproduct'),
     path('adminsaveproduct/',adminsaveproduct, name='adminsaveproduct'),
     path('delete_product/<int:pid>/',delete_product, name='delete_product'),
     path('delete_category/<int:pid>/',delete_category, name='delete_category'),
     path('adminsavecategory/',adminsavecategory, name='adminsavecategory'),

]