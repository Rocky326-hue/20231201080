from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HelloWorldTests(TestCase):
    def test_hello_world_view(self):
        """测试helloworld视图"""
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
    
    def test_hello_name_view(self):
        """测试带参数的helloworld视图"""
        response = self.client.get(reverse('hello_name', args=['Django']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Django!")
    
    def test_index_view(self):
        """测试首页视图"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django Helloworld应用")