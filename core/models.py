from django.db import models

# Create your models here.

class DataTable(models.Model):
    speed = models.CharField(max_length=100,null=True,blank=True)
    driver = models.CharField(max_length=100,null=True,blank=True)
    car = models.CharField(max_length=100,null=True,blank=True)
    engine = models.CharField(max_length=100,null=True,blank=True)
    data = models.CharField(max_length=100,null=True,blank=True)
