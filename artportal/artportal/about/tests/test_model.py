from django.test import TestCase

from artportal.about.models import About


class TestModel(TestCase):
    def test_about_Model(self):
        obj = About.objects.create(
            name='qwe',
            description='test',
            image='images/path/qwe.jpg',
        )
        obj.save()
        self.assertEqual(str(obj), 'qwe')
