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
    file = request.FILES['document']
    if file.content_type != 'text/plain':
        messages.info(request, 'please, index a valid txt file. ')
        return render(request, 'main/base.html', status=406)
        
    # creates an object list that later receives all the objects that were created through the .txt file
    objects_list = []
    cash_amount = []
    total_sum = 0

    # checks if the data is what we are expecting by checking the first line columns; if they match the key_words list, then proceds;
    for n, line in enumerate(file):
        if n == 0:
            key_words = ['comprador', 'descrição', 'preço unitário', 'quantidade', 'endereço', 'fornecedor']

            # creates a list with the first column words by decoding the bytes to string and taking the special chars
            first_line_list = list(map(lambda x: x.decode('utf-8').strip(), line.split(b'\t')))

            # checks if the created list matches the key_words list; if so, keep goin;
            for count, column in enumerate(first_line_list):
                if column.lower() != key_words[count]:
                    print('error within the first line data. ')
                    messages.info(request, 'error within the first line data. ')
                    return render(request, 'main/base.html', {}, status=406)
            continue

        
        # creates a list with all the data that is on the current .txt line, then...
        # creates a model instance using that list and save it
        data_list = list(map(lambda x: x.decode('utf-8').strip(), line.split(b'\t')))
        print(line.split(b'\t'))
        try:
            data_instance = Data(buyer=data_list[0], description=data_list[1], price=float(data_list[2])
                                , quantity=int(data_list[3]), address=data_list[4], suplier=data_list[5].strip())
            data_instance.save()
        except:
            print('error within the received data. ')
            print(data_list)
            messages.info(request, 'error within the received data. ')
            return render(request, 'main/base.html', {}, status=406)
        
        # adds the object to the objects_list, wich will be used as an output
        objects_list.append(data_instance)
        cash_amount.append(data_instance.get_total_product_price())

    # calculates the total cash that was on the data collected
    for n in cash_amount:
        total_sum += n

    messages.info(request, 'data received successfully. ')
    return render(request, 'main/data-list.html', {'object_list': objects_list, 'total_sum': total_sum}, status=201)

def listView(request):
    # queryset
    queryset = Data.objects.all()

    return render(request, 'main/data-list.html', {'object_list': queryset})
