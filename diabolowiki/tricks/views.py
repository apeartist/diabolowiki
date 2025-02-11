from django.shortcuts import render
from .models import Trick

# Create your views here.

def alltricks(request):
    tricks = Trick.objects.all()
    context = {
        'tricks':tricks
    }
    return render(request, 'tricks/alltricks.html', context)

def trick(request, trickname):
    tr = Trick.objects.get(name=trickname)
    context = {
        'trick':tr
    }
    return render(request, 'tricks/trickbase.html', context)