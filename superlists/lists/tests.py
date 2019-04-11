from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/') #Chama a função da view de forma direta
        self.assertTemplateUsed(response, 'home.html') #Verifica qual template foi usado para renderizar uma resposta


