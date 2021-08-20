from django.contrib.auth import get_user_model
from datetime import datetime
from django.test import TestCase

User = get_user_model()


class AccountModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='pesho', password='123')

    def test_model_fields_type(self):
        self.assertIsInstance(self.user1.date_joined, datetime)
        self.assertIsInstance(self.user1.is_active, bool)
        self.assertIsInstance(self.user1.is_staff, bool)
        self.assertIsInstance(self.user1.is_superuser, bool)


class ArtUserModelTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "z"

        self.test_user = User.objects.create_user(
            username=self.username,
        )

    def test_create_user(self):
        assert isinstance(self.test_user, User)

    def test_default_user_is_active(self):
        assert self.test_user.is_active

    def test_default_user_is_staff(self):
        assert not self.test_user.is_staff

    def test_default_user_is_superuser(self):
        assert not self.test_user.is_superuser
