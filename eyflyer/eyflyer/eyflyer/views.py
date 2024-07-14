from django.http import HttpResponse
from django.shortcuts import render
from myAdmin.models import *
def index(request):
   
   datas = {
      'cataegories':Category.objects.all(),
      'Product':AddProduct.objects.all(),
     
   }
   return render(request,"index.html",datas)
def about(request):
   return render(request,"about.html")


