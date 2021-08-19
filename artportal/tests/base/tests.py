from django.contrib.auth import get_user_model
from django.test import TestCase, Client


UserModel = get_user_model()

class ArtportalTestCase(TestCase):
    logged_in_username = 'moni'
    logged_in_user_password = 'svetlio22'


    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username=self.logged_in_username,
            password=self.logged_in_user_password
        )