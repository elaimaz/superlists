from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve é uma função do Django para resolver URLs e descobrir para qual view eles devem ser mapeados.
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() # Cria um objeto HttpRequest
        response = home_page(request) #é passado para a view home_page, que dara uma resposta
        html = response.content.decode('utf8') # É extraido o .content da resposta (os bytes brutos). .decode() converte os bytes em string HTML
        self.assertTrue(html.startswith('<html>')) #Testa se começa com uma tah <html>
        self.assertIn('<title>To-Do lists</title>', html) # testa se tem a tag <title> contendo as palavras To-Do lists
        self.assertTrue(html.endswith('</html>')) #Testa se termina com tag </html>
