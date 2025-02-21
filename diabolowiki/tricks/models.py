from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Trick(models.Model):
    # TODO restrict fields
    # name should check against lowercase, then use titleify in templates

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, default=1)
    #photo = models.ImageField(upload_to='photo', blank=True)
    instructions = ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list)
    tags = models.ManyToManyField("tricks.TrickTag", related_name="tricks_trick_related")

    # clean up the field data (custom)
    def clean(self):
        self.name = self.name.title()
    
    # returns basic description of the trick
    def __str__(self):
        return self.name+": "+('*'*self.difficulty)+" "+self.description

    # creation method to just create a trick with the name
    @classmethod
    def create(cls, name):
        tr = cls(name=name)
        return tr

class TrickTag(models.Model):
    name = models.CharField(max_length=30)

    def clean(self):
        self.name = self.name.lower()
    
    def __str__(self):
        return "#"+self.name

    # creation method to just create a tag with the name
    @classmethod
    def create(cls, name):
        tag = cls(name=name)
        return tag

