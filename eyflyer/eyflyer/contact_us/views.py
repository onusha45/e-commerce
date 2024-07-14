from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def contact(request):
   return render(request,"contact.html")

def Savecontact(request):
   email = request.POST['email']
   name = request.POST['name']
   message = request.POST['message']
   contact = Contactus(name=name, email=email, message=message)
   contact.save()
   print(f"Received form data - Name: {{name}}, Email: {{email}}, Message: {{message}}")
   return render(request,'contact.html' )

   