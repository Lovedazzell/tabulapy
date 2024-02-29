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
                tables = tabula.read_pdf(file, pages='all',stream=True,multiple_tables=True,pandas_options={'header': None})
                
                # getting table 3 data
                for index, row in tables[3].iterrows():
          
                    if len(str(row[0])) > 5:

                        # Saving to data base
                        dt = CompTable(order_number = row[0] , order_time = row[1], trade_no = row[2] , trade_time = str(row[3])[:9], security_description = str(row[3])[8:] , buy_or_sell = row[4],quantity = row[5] , gross_rate =  row[6] ,brokage=  '' , net_rate =  row[7] , closing_rate =  '' , net_total =  row[8]  , remarks = ''  )
                        dt.save()

                # getting table 4 data
                for index, row in tables[4].iterrows():
                    if len(str(row[0])) > 5:

                        # Saving to data base
                        dt = CompTable(order_number = row[0] , order_time = row[1], trade_no = row[2] , trade_time = str(row[3])[:9], security_description = str(row[3])[8:] , buy_or_sell = row[4],quantity = row[5] , gross_rate =  row[6] ,brokage=  '' , net_rate =  row[7] , closing_rate =  '' , net_total =  row[8]  , remarks = ''  )
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
