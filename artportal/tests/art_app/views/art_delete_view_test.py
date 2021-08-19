from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from artportal.art_auth.models import ArtUser
from tests.base.tests import ArtportalTestCase

UserModel = get_user_model()


class AccountDeleteTest(ArtportalTestCase, TestCase):
    def test_delete_art(self):
        user = ArtUser.objects.create(username='Test user', password='123')
        self.client.force_login(user=user)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
