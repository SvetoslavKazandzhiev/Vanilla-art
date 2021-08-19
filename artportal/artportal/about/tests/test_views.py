from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):
    def test_about_view_GET(self):
        client = Client()
        response = client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')