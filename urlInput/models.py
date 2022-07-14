import datetime
from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your models here.


class Link(models.Model):
    link_text = models.CharField(max_length=200)
    link_status_code = models.BooleanField(default=False, blank=True, null=True)

    class Meta:  
        db_table = "link"

    def __str__(self):
        return self.link_text
 

class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name


