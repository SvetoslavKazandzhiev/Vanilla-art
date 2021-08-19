from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class IndexViewTest(TestCase):
    def test_view_test(self):
        self.client = Client()
        User.objects.create_user(username='fred', password='secret')
        self.client.login(username='fred', password='secret')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)