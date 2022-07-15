from django.test import TestCase ,Client
from django.urls import reverse
from urlInput.models import Link
import json


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('index')
        self.new_url = reverse('new')
        self.edit_url = reverse('edit', args=['1'])
        self.update_url = reverse('update', args=['1'])
        self.delete_url = reverse('delete', args=['1'])
        

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'urlInput/show.html')

    
    def test_project_new_POST(self):
        response = self.client.get(self.new_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'urlInput/index.html')

    def test_project_edit_POST(self):
        response = self.client.post(self.edit_url)

        self.assertEquals(response.status_code ,404)
        self.assertTemplateNotUsed(response, 'urlInput/edit.html')

    # def test_project_update_POST(self):
    #     response = self.client.post(self.update_url)

    #     self.assertEquals(response.status_code, 404)
        
    
    # def test_project_delete_POST(self):
    #     response = self.client.get(self.delete_url)

    #     self.assertEquals(response.status_code, 404)
    #     self.assertRedirects(response, "/urlInput/")