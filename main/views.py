from django.http import HttpResponse
from django.shortcuts import render
from .models import Data
from django.contrib import messages

# Create your views here.
def homeView(request):
    # gets the file and verifies if it's a .txt file; if so, proceds;
    if request.method == 'POST':
        file = request.FILES['document']
        if file.content_type == 'text/plain':
            # creates an object list that later receives all the objects that were created through the .txt file
            objects_list = []
            cash_amount = []
            total_sum = 0

            # checks if the data is what we are expecting by checking the first line columns; if they match the key_words list, then proceds;
            for n, line in enumerate(file):
                if n == 0:
                    key_words = ['comprador', 'descrição', 'preço unitário', 'quantidade', 'endereço', 'fornecedor']
                    first_line_list = list(map(str.strip, line.decode('latin-1').split('\t')))
                    for count, column in enumerate(first_line_list):
                        if column.lower() != key_words[count]:
                            print('error within the received data. ')
                            messages.info(request, 'error within the received data. ')
                            return render(request, 'main/base.html', {}, status=406)
                    continue

                
                # decodes, creates a model instance with the data information, save it and then appends it to the objects_list
                data_list = str(line.decode('latin-1')).split('\t')
                data_instance = Data(buyer=data_list[0], description=data_list[1], price=float(data_list[2])
                                    , quantity=int(data_list[3]), address=data_list[4], suplier=data_list[5].strip())
                data_instance.save()
                
                objects_list.append(data_instance.get_data_list())
                cash_amount.append(data_instance.get_total_product_price())

            # calculates the total cash
            for n in cash_amount:
                total_sum += n

            # displays a list with all the received data and the total amount
            print(f'List of registered objects: \n{objects_list}')
            print(f'total amount: {total_sum}')

            messages.info(request, 'data received successfully. ')
            status = 201

        else:
            messages.info(request, 'please, index a valid txt file. ')
            status = 406

    else:
        status = 200
    return render(request, 'main/base.html', status=status)

def listView(request):
    # queryset
    queryset = Data.objects.all()

    return render(request, 'main/data-list.html', {'object_list': queryset})