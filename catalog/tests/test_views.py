from django.test import TestCase, Client
from django.urls import reverse

from model_bakery import baker

from catalog.models import Product, Category

class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = baker.make('catalog.Product', _quantity = 10)

    def tearDow(self):
        Product.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        product_list = response.context['products']
        #self.assertEquals(product_list.count(), 3)

    def test_page_not_found(self):
        response = self.client.get('/templates/catalog')
        self.assertEquals(response.status_code, 404)