from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()


# class TestLogout(TestCase):
#     def test_logout(self):
#         # self.client = Client()
        # self.user1 = User.objects.create_user(username='fred', password='secret')
        # self.client.login(username='fred', password='secret')
        # response = self.client.get(reverse('log out user'))
        # self.assertEqual(response.status_code, 302)

        # self.client.force_login(self.user1)
        # self.client.logout()
        # response = self.client.post(reverse('log out user'))
        # self.assertEqual(response.status_code, 302)

class TestSignOutView(TestCase):
    def test_successful_signOut(self):
        self.user1 = User.objects.create_user(username='fred', password='secret')
        self.client.force_login(self.user1)
        self.client.logout()
        response = self.client.post(reverse('log out user'))
        self.assertEqual(response.status_code, 302)