from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class ArtUserTest(TestCase):
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



