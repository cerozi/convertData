from django.db import models
from django.contrib import messages

# Create your models here.
class Data(models.Model):
    buyer = models.CharField(max_length=55)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    suplier = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.description} - {self.buyer}'

    def get_total_product_price(self):
        return self.quantity * self.price

    def save_data(self, n, line):
        # checks if the data is what we are expecting by checking the first line columns; if they match the key_words list, then proceds;
        if n == 0:
            key_words = ['comprador', 'descrição', 'preço unitário', 'quantidade', 'endereço', 'fornecedor']

            # creates a list with the first column words by decoding the bytes to string and taking the special chars
            first_line_list = list(map(lambda x: x.decode('utf-8').strip(), line.split(b'\t')))
            print(first_line_list)

            # checks if the created list matches the key_words list;
            for count, column in enumerate(first_line_list):
                if column.lower() != key_words[count]:
                    return [False, 'error within the first line data. ']
            return [None]
            
        # creates a list with all the data that is on the current .txt line, then...
        # creates a model instance using that list and save it
        data_list = list(map(lambda x: x.decode('utf-8').strip(), line.split(b'\t')))
        print(data_list)
        try:
            self = Data(buyer=data_list[0], description=data_list[1], price=float(data_list[2])
                                , quantity=int(data_list[3]), address=data_list[4], suplier=data_list[5].strip())
            self.save()
            return [True, self, self.get_total_product_price()]
        except:
            return [False, f'error within the line data: {n + 1}. ']