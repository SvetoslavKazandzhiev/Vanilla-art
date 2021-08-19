from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from artportal.art_app.models import Art
from artportal.art_auth.models import Account
from tests.base.tests import ArtportalTestCase

UserModel = get_user_model()





class AccountDetailsTest(ArtportalTestCase):
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
        # self.assertEqual(path_to_image, account.profile_image.path)

    def test_postDetails_whenUserLoggedInwithImage_change_images(self):
        path_to_image = 'path/to/image.png'
        account = Account.objects.get(pk=self.user.id)
        account.profile_image = path_to_image+'old'
        account.save()
        self.client.force_login(self.user)

        response = self.client.post(reverse('view profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)
        account = Account.objects.get(pk=self.user.id)
        # self.assertEqual(path_to_image, account.profile_image.path)