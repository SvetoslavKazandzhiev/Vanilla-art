from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tests.base.mixins import ArtTestUtils
from tests.base.tests import ArtportalTestCase

User = get_user_model()

class RegisterViewTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.password = 'password'

    def test_createArt_withoutCreatedProfile_form(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/register.html')

    def test_createArt_withCreatedProfile_form(self):
        self.client = Client()
        User.objects.create_user(username='fred', password='secret')
        self.client.login(username='fred', password='secret')
        response = self.client.get(reverse('log in user'))

        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)