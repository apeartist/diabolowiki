from django.shortcuts import render
from django.core.mail import mail_admins
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
        mail_admins(subject,message,settings.DEFAULT_FROM_EMAIL,fail_silently=False)
    return render(request,"contact.html")