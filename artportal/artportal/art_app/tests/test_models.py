
from PIL import Image
from django.contrib.auth import get_user_model
from django.test import TestCase

from artportal.art_app.models import Art
from artportal.art_auth.views import User

UserModel = get_user_model()

class TestartModel(TestCase):
    def test_model_fields_type(self):
        self.user = User.objects.create_user(username='fred', password='secret')
        self.art = Art.objects.create(
          name='Test name',
          description='Test description',
           image='path/to/image.png',
           type=Art.PHOTOGRAPHY,
            user=self.user,
        )
        self.assertIsInstance(self.art.name, str)
        self.assertIsInstance(self.art.description, str)
        self.assertIsInstance(self.art.type, str)
        self.assertTrue(self.art.image, Image)

