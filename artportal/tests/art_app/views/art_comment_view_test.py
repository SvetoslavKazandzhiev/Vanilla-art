
from django.test import TestCase

from artportal.art_app.forms import CommentForm
from artportal.art_app.models import Art
from tests.base.mixins import UserTestUtils


class CommentViewTest(UserTestUtils, TestCase):

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