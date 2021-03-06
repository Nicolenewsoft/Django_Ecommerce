from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.conf import settings
from core.forms import ContactForm


from model_bakery import baker

User = get_user_model()
#Iniciando o teste para o index
class IndexViewTestCase(TestCase): #TestCase, tipo de teste django baseados em classe
    #dentro do TestCase, chamamos o Client
    #Client atua como um cliente testando requisições, como GET, POST, urls, requerimentos... 
    def setUp(self): 
        self.client = Client()
        self.url = reverse('index') #testando url do index

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200) #testando o status 200(sucess)
    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html') #testando a usuabilidade do template


class ContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(assertFormError):
        field = {'name': ' ', 'email': '', 'message': ''}
        #response = self.client.post(self.url, data)
        if field:
            field = "Este campo é obrigatório "
        #self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        #self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        #self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def tet_form_ok(self):
        data = {'name': 'test', 'message': 'test', 'email': 'test@test.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['sucess'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do Django E-Commerce')


