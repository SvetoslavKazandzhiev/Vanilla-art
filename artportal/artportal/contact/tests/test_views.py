from django.test import TestCase, Client
from django.urls import reverse


class TestContactView(TestCase):
    def test_contact_view_GET(self):
        client = Client()
        response = client.get(reverse('contact view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')