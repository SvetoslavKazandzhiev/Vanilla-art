
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()
from artportal.art_app.models import Art
from artportal.art_auth.models import Account

UserModel = get_user_model()

from artportal.art_auth.models import ArtUser
from tests.base.tests import ArtportalTestCase


class AccountDeleteViewTest(ArtportalTestCase, TestCase):
    def test_delete_art(self):
        user = ArtUser.objects.create(username='Test user', password='123')
        self.client.force_login(user=user)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class DeleteAccountViewTest(TestCase):
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


class AccountDetailsViewTest(ArtportalTestCase):
    def test_getDetails_whenLoggedInUser_shouldGetDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('view profile details'))
        self.assertListEmpty(list(response.context['arts']))
        self.assertEqual(self.user.id, response.context['account'].user_id)

    def test_getDetails_whenLoggedInUserWithArts_shouldGetDetails(self):
        art = Art.objects.create(
            name='Test name',
            description='Test description',
            image='path/to/image.png',
            type=Art.PHOTOGRAPHY,
            user=self.user,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('view profile details'))

        self.assertEqual(self.user.id, response.context['account'].user_id)
        self.assertListEqual([art], list(response.context['arts']))

    def test_postDetails_whenUserLoggedInwithoutImage_change_images(self):
        path_to_image = 'path/to/image.png'
        self.client.force_login(self.user)

        response = self.client.post(reverse('view profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)
        account = Account.objects.get(pk=self.user.id)

    def test_postDetails_whenUserLoggedInwithImage_change_images(self):
        path_to_image = 'path/to/image.png'
        account = Account.objects.get(pk=self.user.id)
        account.profile_image = path_to_image + 'old'
        account.save()
        self.client.force_login(self.user)

        response = self.client.post(reverse('view profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)
        account = Account.objects.get(pk=self.user.id)


class LogInUserViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='fred', password='secret')

    def test_successful_Log_In(self):
        self.client.force_login(self.user1)
        user = auth.get_user(self.client)
        response = self.client.get(reverse('index'))
        self.assertTrue(user.is_authenticated)
        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_Log_In(self):
        self.client.login(username='aaa', password='qwer1234')
        user = auth.get_user(self.client)
        data = {'user': user}
        response = self.client.post(reverse('log in user'), data)
        self.assertTrue(not user.is_authenticated)
        self.assertEqual(response.status_code, 200)


class SignOutViewTest(TestCase):
    def test_successful_sign_Out(self):
        self.user1 = User.objects.create_user(username='fred', password='secret')
        self.client.force_login(self.user1)
        self.client.logout()
        response = self.client.post(reverse('log out user'))
        self.assertEqual(response.status_code, 302)


class SignUpViewTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.password = 'password'

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/register.html')