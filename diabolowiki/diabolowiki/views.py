from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def conventions(request):
    return render(request,"conventions.html")