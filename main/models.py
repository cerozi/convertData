from django.db import models

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

    def get_data_list(self):
        return [self.buyer, self.description, self.price, self.quantity, self.address, self.suplier]