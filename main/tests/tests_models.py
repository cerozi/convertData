# django imports

from django.test import TestCase
from django.urls import reverse

# app imports

from main.models import Data

class DataModelTest(TestCase):

    def setUp(self):
        self.data_obj = Data.objects.create(
            buyer='Matheus',
            description='R$10 off R$20 of food',
            price=10.0,
            quantity=2,
            address='Rua do Tatuapé, 343',
            suplier='Ifood',

        )

    # testing models functions
    def test_get_total_product_price(self):
        self.assertEqual(self.data_obj.get_total_product_price(), 20.0)

    def test_get_data_list(self):
        self.assertEqual(len(self.data_obj.get_data_list()), 6)