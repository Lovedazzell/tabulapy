from django.contrib import admin
from . models import DataTable,CompTable
# Register your models here.


@admin.register(DataTable)
class AdminCompTable(admin.ModelAdmin):
    list_display = ['speed','driver','car','engine','data']


@admin.register(CompTable)
class AdminCompTable(admin.ModelAdmin):
    list_display = [  'order_number', 'order_time' , 'trade_no', 'trade_time', 
    'security_description' , 'buy_or_sell', 'quantity', 'gross_rate', 'brokage',
    'closing_rate', 'net_total', 'remarks' ]




