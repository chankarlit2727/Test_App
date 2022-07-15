from django.urls import resolve, reverse
from django.test import SimpleTestCase
from urlInput.views import index,new,edit,update,delete 

class TestUrl(SimpleTestCase):

    def test_link_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_new_url_is_resolved(self):
        url = reverse('new')
        self.assertEquals(resolve(url).func, new)
    
    def test_edit_url_is_resolved(self):
        url = reverse('edit', args=['1'])
        self.assertEquals(resolve(url).func, edit)
    
    def test_update_url_is_resolved(self):
        url = reverse('update', args=['1'])
        self.assertEquals(resolve(url).func, update)
    
    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=['1'])
        self.assertEquals(resolve(url).func, delete)
