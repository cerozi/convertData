# django imports

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# app imports

from .models import Data


# Create your views here.
def homeView(request):
    
    if request.method != 'POST':
        return render(request, 'main/base.html')
    
    # gets the file and verifies if it's a .txt file; if so, proceds;
    try:
        file = request.FILES['document']
    except:
        messages.info(request, 'please, certify to index a file. ')
    if file.content_type != 'text/plain':
        messages.info(request, 'please, index a valid txt file. ')
        return render(request, 'main/base.html', status=406)
        
    # creates an object list that later receives all the objects that were created through the .txt file
    objects_list = []
    cash_amount = []
    total_sum = 0

    # iterates from each .txt line to save the objects;
    for n, line in enumerate(file):
        from .models import Data
        line_info = Data.save_data(None, n, line)
        if line_info[0] == False:
            messages.info(request, line_info[1])
            return render(request, 'main/base.html', status=406)

        # adds the object to the objects_list, wich will be used as an output
        if line_info[0] == True:
            objects_list.append(line_info[1])
            cash_amount.append(line_info[2])

    # calculates the total cash that was on the data collected
    for n in cash_amount:
        total_sum += n

    messages.info(request, 'data received successfully. ')
    return render(request, 'main/data-list.html', {'object_list': objects_list, 'total_sum': total_sum}, status=201)

def listView(request):
    # queryset
    queryset = Data.objects.all()

    return render(request, 'main/data-list.html', {'object_list': queryset})
