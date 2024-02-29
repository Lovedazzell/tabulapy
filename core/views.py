from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . forms import PdfReceiver
import tabula
import tempfile
from . models import DataTable
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
                messages.error(request,'Something went wrong')

            return HttpResponseRedirect('/')
    else:
        form = PdfReceiver()
    
    context = {'form': form}
    return render(request, 'core/home.html', context)