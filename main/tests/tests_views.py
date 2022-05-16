from django.test import TestCase
from django.urls import reverse

class HomeViewTests(TestCase):

    # GET method
    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/base.html')

    # POST method
    def test_home_POST(self):

        # correct file
        with open('right_txt_data_for_test.txt', 'rb') as document:
            response = self.client.post(reverse('home'), data={'document': document})
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'main/base.html')

        # wrong file
        with open('wrong_txt_data_for_test.txt', 'rb') as document:
            response = self.client.post(reverse('home'), data={'document': document})
        self.assertEqual(response.status_code, 406)
        self.assertTemplateUsed(response, 'main/base.html')

class ListViewTests(TestCase):

    # GET method
    def test_list_GET(self):
        response = self.client.get(reverse('data-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/data-list.html')