from django.contrib.auth import get_user_model

User = get_user_model()

from datetime import datetime

from django.test import TestCase


class TestAccountModel(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='pesho', password='123')

    def test_model_fields_type(self):
        self.assertIsInstance(self.user1.date_joined, datetime)
        self.assertIsInstance(self.user1.is_active, bool)
        self.assertIsInstance(self.user1.is_staff, bool)
        self.assertIsInstance(self.user1.is_superuser, bool)


