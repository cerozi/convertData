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
    
    # testing if it creates a new model after the uploading of a file
    # correct file data
    def test_object_created_after_correct_data_post(self):
        with open('right_txt_data_for_test.txt', 'rb') as document:
            response = self.client.post(reverse('home'), data={'document': document}) # create a model object
        self.assertEqual(Data.objects.count(), 2)
        self.assertEqual(response.status_code, 201)

    # wrong file data
    def test_object_not_created_after_wrong_data_post(self):
        with open('wrong_txt_data_for_test.txt', 'rb') as document:
            response = self.client.post(reverse('home'), data={'document': document}) # dont create a model object
        self.assertEqual(Data.objects.count(), 1)
        self.assertEqual(response.status_code, 406)
