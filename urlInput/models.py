import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Link(models.Model):
    link_text = models.CharField(max_length=200)
    link_status_code = models.CharField(max_length=100)

    class Meta:  
        db_table = "link"

    def __str__(self):
        return self.link_text
 

class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name


