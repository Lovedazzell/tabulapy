from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . forms import PdfReceiver
import tabula
import tempfile
from . models import DataTable , CompTable
import os
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = PdfReceiver(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['data']
            
            try:
                tables = tabula.read_pdf(file, pages='all',multiple_tables=True)
                
                for index, row in tables[1].iterrows():
                    data = DataTable.objects.create(speed= row[0],driver= row[1],car=row[2],engine=row[3],data=row[4])
                messages.success(request,'File saves successfully')
            except Exception as e:
                print("Error:============",e)
                messages.error(request,'Something went Wrong')

            return HttpResponseRedirect('/')
    else:
        form = PdfReceiver()
    
    context = {'form': form}
    return render(request, 'core/home.html', context)

# Complex Layout
def comp(request):
    if request.method == 'POST':
        print('POST ===============')
        form = PdfReceiver(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['data']
            
            try:
                tables = tabula.read_pdf(file, pages='all',multiple_tables=True)
               

                for index, row in tables[0].iterrows():
                    if row[0] == 'OUTSCAN Performance' or  row[0] == 'Service Centre' or index + 1 == len(tables[0]):
                        continue
                    
                    dt = CompTable(service_center = row[0] , fresh = row[1], overall_conversion = row[2] , rvp_done = row[3] , eds = row[4] , eds_conversion = row[5],rvp = row[6]  )
                    dt.save()
                    
                messages.success(request,'File saves successfully')
            except Exception as e:
                print("Error:============",e)
                messages.error(request,'Something went Wrong')

            return HttpResponseRedirect('/comp/')
    else:
        form = PdfReceiver()
    
    context = {'form': form}
    return render(request, 'core/comp.html', context)
