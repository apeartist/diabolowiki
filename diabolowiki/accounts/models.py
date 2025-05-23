from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to="accounts/images/")
    description = models.TextField(blank=True, null=True)

