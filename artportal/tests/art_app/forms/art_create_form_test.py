from django.test import TestCase, Client
from django.urls import reverse


class CreateFormTest(TestCase):
    def test_createform_if_is_valid(self):
        client = Client()
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 302)