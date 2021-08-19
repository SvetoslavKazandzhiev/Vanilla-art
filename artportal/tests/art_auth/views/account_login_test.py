from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
#
# from tests.base.tests import ArtportalTestCase
#
#
# class LogInTest(ArtportalTestCase, TestCase):
#     def test_login_withAlready_created_profile(self):
#         self.client.force_login(self.user)
#
#         response = self.client.get(reverse('index'))
#         self.assertTrue(self.user.id, response.context['user'].id)
#
#     def test_login_without_created_profile(self):
#         self.client.force_login(self.user)
#
#         response = self.client.get(reverse('log in user'))
#         self.assertTrue(self.user.id, response.context['user'].id)



User = get_user_model()


class TestSighInView(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='fred', password='secret')


    # def test_get_log_In_view(self):
    #     response = self.client.get(reverse('log in user'))
    #     self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Please fill all the fields to Sign In')


    def test_successful_Log_In(self):
    #     self.client.login(username='sss', password='test1234')
    #     user = User.objects.create_user(username='fred', password='secret')
    #     data = {'user': user}
    #     response = self.client.post(reverse('index'), data)
    #     self.assertTrue(user.is_authenticated)
    #     # self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user1)
        user = auth.get_user(self.client)
        response = self.client.get(reverse('index'))
        self.assertTrue(user.is_authenticated)
        self.assertEqual(response.status_code, 200)


    def test_unsuccessful_signIn(self):
        self.client.login(username='aaa', password='qwer1234')
        user = auth.get_user(self.client)
        data = {'user': user}
        response = self.client.post(reverse('log in user'), data)
        self.assertTrue(not user.is_authenticated)
        self.assertEqual(response.status_code, 200)