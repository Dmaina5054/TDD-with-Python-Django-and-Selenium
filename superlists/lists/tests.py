from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.
#here we define our unittests
#run and see failure behavior
#write code and address current fail
class HomePageTest(TestCase):
    """we use django test client here and then 
    confirm we can resolve our view"""
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
        
    #can we resolve a url from /
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
        
    #use django test_client
    #check if template used is home.html
    # def test_home_page_return_correct_html(self):
    #     response = self.client.get('/') #instead of earlier instantiating HttpRequest call view func
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.strip().endswith('</html>'))
        
    #     self.assertTemplateUsed(response,'home.html') #the magic
        
        
        
    # def test_home_page_return_correct_html(self):
    #     request = HttpRequest() #whatever passed to django view
    #     response = home_page(request)
    #     html = response.content.decode('utf-8')
    #     self.assertTrue(html.startswith('<html>')) #now resolve true
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertIn('<h1>To-Do</h1>', html)
    #     self.assertTrue(html.endswith('</html>'))
    
    #METHOD 1
    
    # def test_home_page_return_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf-8')
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(html,expected_html)
        
        
        
        
