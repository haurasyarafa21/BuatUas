from django.db import models

# Create your models here.
class Item(models.Model):
   name = models.TextField(default='')
   number = models.TextField(default='')
