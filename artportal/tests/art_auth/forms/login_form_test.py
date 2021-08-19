from django.test import TestCase, Client
from django.urls import reverse


class LoginFormTest(TestCase):
    def test_form(self):
        client = Client()
        response = self.client.get(reverse('log in user'))
        self.assertEqual(response.status_code, 200)

