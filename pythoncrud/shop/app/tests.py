from urllib import response
from django.test import client
from django.urls import reverse
from django.test import TestCase

# Create your tests here.
class Testciew(TestCase):
    def test_create(self):
        url=reverse('create')
        data={
            'first_name':'shivam',
            'last_name':'verma',
            'email':'shivam@gmail.com',
            'address':'fazilka',
            'mobile':'7888545377'
        }
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,302)
        response=self.client.get(url,data)
        self.assertEqual(response.status_code,200)
    
