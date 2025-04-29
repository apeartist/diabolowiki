from django.shortcuts import render
from django.contrib import messages
from django import forms
from .models import Trick

# Create your views here.

def alltricks(request):
    tricks = Trick.objects.all()
    if request.GET:
        query = request.GET.get('search')
        tricks = Trick.objects.filter(name__icontains=query)
    context = {
        'tricks':tricks
    }
    return render(request, 'tricks/alltricks.html', context)

def trick(request, trickname):
    tr = Trick.objects.get(slug=trickname)
    first = tr.history.first()
    if first.prev_record:
        hist = first.diff_against(first.prev_record).changes
    else:
        hist = None
    context = {
        'trick':tr,
        'history': first,
        'history_changes': hist,
    }
    return render(request, 'tricks/trickbase.html', context)

def edittrick(request, trickname):
    if request.method == "POST":
        counter=0
        instr = request.POST["instruction"+str(counter)]
        while instr!="":
            print(instr)
            counter+=1
            try:
                instr = request.POST["instruction"+str(counter)]
            except:
                break
        if instr=="": # it stopped because there was something empty
            messages.error(request, "Instructions cannot be empty!")
        pass # put in editing code here
    tr = Trick.objects.get(slug=trickname)
    context = {
        'trick':tr
    }
    return render(request, 'tricks/edittrick.html', context)