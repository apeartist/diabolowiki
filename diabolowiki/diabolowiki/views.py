from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request,'index.html')

def conventions(request):
    return render(request,"conventions.html")

def contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,["apeartistemail@gmail.com"],fail_silently=False)
    return render(request,"contact.html")