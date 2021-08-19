from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from artportal.art_auth.models import ArtUser

UserModel = get_user_model()

User = get_user_model()


class TestDeleteAccountView(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='pesho', password='123')

    def test_delete_account_view(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('user confirm delete', args=(self.user1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_successful_delete_account(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse('user confirm delete', args=(self.user1.id,)))
        self.assertEqual(response.status_code, 302)
