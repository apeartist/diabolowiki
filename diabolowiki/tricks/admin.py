from django.contrib import admin

# Register your models here.
from .models import Trick

class TrickAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}

admin.site.register(Trick, TrickAdmin)