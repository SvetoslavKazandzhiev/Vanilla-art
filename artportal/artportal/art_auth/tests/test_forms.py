from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()


class LoginFormTest(TestCase):
    def test_form(self):
        client = Client()
        response = self.client.get(reverse('log in user'))
        self.assertEqual(response.status_code, 200)


class SignUpFormTest(TestCase):
    def test_signup_form(self):
        self.client = Client()
        User.objects.create_user(username='fred', password='secret')
        self.client.login(username='fred', password='secret')
        response = self.client.get(reverse('register user'))

        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
