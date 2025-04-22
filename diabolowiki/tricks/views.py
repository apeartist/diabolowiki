from django.shortcuts import render
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
    context = {
        'trick':tr,
        'history': first,
        'history_changes': first.diff_against(first.prev_record).changes,
    }
    return render(request, 'tricks/trickbase.html', context)

def edittrick(request, trickname):
    if request.method == "POST":
        pass # put in editing code here
    tr = Trick.objects.get(slug=trickname)
    context = {
        'trick':tr
    }
    return render(request, 'tricks/edittrick.html', context)