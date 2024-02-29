from django.db import models

# Create your models here.

class DataTable(models.Model):
    speed = models.CharField(max_length=100,null=True,blank=True)
    driver = models.CharField(max_length=100,null=True,blank=True)
    car = models.CharField(max_length=100,null=True,blank=True)
    engine = models.CharField(max_length=100,null=True,blank=True)
    data = models.CharField(max_length=100,null=True,blank=True)


class CompTable(models.Model):
    service_center = models.CharField(max_length=100,null=True,blank=True)
    fresh = models.CharField(max_length=100,null=True,blank=True)
    overall_conversion = models.CharField(max_length=100,null=True,blank=True)
    rvp_done = models.CharField(max_length=100,null=True,blank=True)
    eds = models.CharField(max_length=100,null=True,blank=True)
    eds_conversion = models.CharField(max_length=100,null=True,blank=True)
    rvp = models.CharField(max_length=100,null=True,blank=True)
