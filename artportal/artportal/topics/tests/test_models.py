from PIL import Image
from django.test import TestCase
from artportal.art_app.models import Art
from artportal.topics.models import Topics


class TopicModelTest(TestCase):
    def test_topic_model_fields(self):
        self.topic = Topics.objects.create(
          name='Test name',
          description='Test description',
           image='path/to/image.png',
           topic_type=Topics.PHOTOGRAPHY,
        )
        self.assertIsInstance(self.topic.name, str)
        self.assertIsInstance(self.topic.description, str)
        self.assertIsInstance(self.topic.topic_type, str)
        self.assertTrue(self.topic.image, Image)

