from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import permission_required, login_required
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

@login_required
@permission_required("trick.can_edit")
def edittrick(request, trickname):

    tr = Trick.objects.get(slug=trickname)

    if request.method == "POST":
        description = request.POST['description']
        difficulty = request.POST['difficulty']

        counter=0
        instr = [request.POST["instruction"+str(counter)],]
        while instr[counter]!="":
            counter+=1
            try:
                instr.append(request.POST["instruction"+str(counter)])
            except:
                counter-=1
                break
        if counter==0: # it stopped because there was something empty
            messages.error(request, "Instructions cannot be empty!")

        tr.description=description
        tr.difficulty = difficulty
        tr.instructions=instr
        tr.save()
        messages.success(request, "Successfully edited trick!")
        return redirect('tricks:tricks-page', trickname=tr.slug)
        
    context = {
        'trick':tr
    }
    return render(request, 'tricks/edittrick.html', context)

@login_required
@permission_required("trick.can_edit")
def newtrick(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        difficulty = request.POST['difficulty']

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
        print('made new trick')
        newtrick = Trick(name=name,description=description,difficulty=difficulty,instructions=instr)
        newtrick.save()
    return render(request, 'tricks/edittrick.html')