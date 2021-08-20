from django.contrib.auth import get_user_model
from django.test import TestCase
from artportal.art_app.forms import ArtCreateForm, CommentForm
from artportal.art_app.models import Art
from tests.base.mixins import UserTestUtils

User = get_user_model()


class TestArtCreateForm(TestCase):
    def test_art_create_form_without_valid(self):

        art = ArtCreateForm(data={
            'type': 'fine_art',
            'name': '123',
            'description': 'test',
            'image': 'image/path/to/image.jpg',
        })
        self.assertFalse(art.is_valid())

    def test_art_create_form_with_valid(self):
        pass



class CommentFormTest(UserTestUtils, TestCase):

    def test_if_comment_form_is_valid(self):
        art_user = self.create_user(username='222',password='222')

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

class TestEditArtForm(TestCase):
        pass

class TestDeleteArtForm(TestCase):
        pass

class TestCommentFormTest(TestCase):
        pass
