from django.contrib.postgres.forms import SimpleArrayField
from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Textarea

class TrickForm(forms.ModelForm):
    instructions = SimpleArrayField(CharField(), delimiter='\n', widget=Textarea())