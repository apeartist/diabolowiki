from django.contrib import admin

# Register your models here.
from .models import Trick, TrickTag
from .forms import TrickForm

class TrickAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}
    form = TrickForm

admin.site.register(Trick, TrickAdmin)
admin.site.register(TrickTag)