from django.test import TestCase, Client
from django.urls import reverse


class CreateUrlTest(TestCase):
    def test_Create_urls_if_is_valid(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 302)