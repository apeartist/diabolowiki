from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Trick(models.Model):
    # TODO restrict fields
    # name should check against lowercase, then use titleify in templates

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 5)], blank=True, default=1)
    #photo = models.ImageField(upload_to='photo', blank=True)
    instructions = ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list)

    def __str__(self):
        return self.name+": "+self.description
