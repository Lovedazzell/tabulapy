from django.contrib import admin
from . models import DataTable,CompTable
# Register your models here.


@admin.register(DataTable)
class AdminCompTable(admin.ModelAdmin):
    list_display = ['speed','driver','car','engine','data']


@admin.register(CompTable)
class AdminCompTable(admin.ModelAdmin):
    list_display = [  'service_center', 'fresh' , 'overall_conversion', 'rvp_done', 'eds', 'eds_conversion','rvp' ]




