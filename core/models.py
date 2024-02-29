from django.db import models

# Create your models here.

class DataTable(models.Model):
    speed = models.CharField(max_length=100,null=True,blank=True)
    driver = models.CharField(max_length=100,null=True,blank=True)
    car = models.CharField(max_length=100,null=True,blank=True)
    engine = models.CharField(max_length=100,null=True,blank=True)
    data = models.CharField(max_length=100,null=True,blank=True)


class CompTable(models.Model):
    order_number = models.CharField(max_length=100,null=True,blank=True)
    order_time = models.CharField(max_length=100,null=True,blank=True)
    trade_no = models.CharField(max_length=100,null=True,blank=True)
    trade_time = models.CharField(max_length=100,null=True,blank=True)
    security_description = models.CharField(max_length=100,null=True,blank=True)
    buy_or_sell = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.CharField(max_length=100,null=True,blank=True)
    gross_rate = models.CharField(max_length=100,null=True,blank=True)
    brokage = models.CharField(max_length=100,null=True,blank=True)
    net_rate = models.CharField(max_length=100,null=True,blank=True)
    closing_rate = models.CharField(max_length=100,null=True,blank=True)
    net_total = models.CharField(max_length=100,null=True,blank=True)
    remarks = models.CharField(max_length=100,null=True,blank=True)
