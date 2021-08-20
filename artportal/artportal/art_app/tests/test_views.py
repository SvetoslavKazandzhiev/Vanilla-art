from artportal.art_app.forms import CommentForm
from tests.base.mixins import ArtTestUtils, UserTestUtils
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from artportal.art_app.models import Art
from tests.base.tests import ArtportalTestCase

User = get_user_model()


class CommentViewTest(UserTestUtils, TestCase):
    def test_if_comment_form_is_valid(self):
        art_user = self.create_user(username='222', password='222')

        art = Art.objects.create(
            name='Test name',
            description='Test description',
            image='path/to/image.png',
            type=Art.PHOTOGRAPHY,
            user=art_user,
        )

        form_data = {'description': 'description', 'art': art.pk}
        form = CommentForm(form_data)
        form.fields['text'].initial = art

        self.assertFalse(form.is_valid())


class ArtCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.password = 'password'

    def test_createArt_withoutCreatedProfile_form(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/register.html')

    def test_createArt_withCreatedProfile_form(self):
        self.client = Client()
        User.objects.create_user(username='fred', password='secret')
        self.client.login(username='fred', password='secret')
        response = self.client.get(reverse('log in user'))

        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)


class ArtDetailsViewTest(ArtTestUtils, UserTestUtils, ArtportalTestCase):
    def test_getArtDetails_whenArtDoesnotexistAndis_owner_return_detailsforOwner(self):
        self.client.force_login(self.user)
        art = self.create_art(
            name='Test name',
            description='Test description',
            image='path/to/image.png',
            type=Art.PHOTOGRAPHY,
            user=self.user,
        )

        response = self.client.get(reverse('details art img', kwargs={
            'pk': art.id,
        }))

        self.assertTrue(response.context['is_owner'])

    def test_getArtDetails_whenArtexistAndis_owner_return_detailsforOwner(self):
        self.client.force_login(self.user)
        art = self.create_art(
            name='Test name',
            description='Test description',
            image='path/to/image.png',
            type=Art.PHOTOGRAPHY,
            user=self.user,
        )

        response = self.client.get(reverse('details art img', kwargs={
            'pk': art.id,
        }))

        self.assertTrue(response.context['is_owner'])
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class IndexViewTest(TestCase):
    def test_index_view_GET(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
