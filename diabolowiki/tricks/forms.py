from django.contrib.postgres.forms import SimpleArrayField
from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Textarea
from tricks.models import *

class TrickForm(forms.ModelForm):
    class Meta:
        model = Trick
        fields = ["description", "difficulty", "instructions", "tags"]
    
    instructions = SimpleArrayField(CharField(), delimiter='\n', widget=Textarea())
    