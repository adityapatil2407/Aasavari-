from django.shortcuts import render
from django.http import HttpResponse
from Tea.models import ContactMessage

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        contact_message=ContactMessage(name=name,email=email,message=message)
        contact_message.save()

        return HttpResponse("Thank you for your message! We will get back to you soon.")
     
    return render(request,'contact.html')

    

def services(request):
    return render(request, 'services.html')
