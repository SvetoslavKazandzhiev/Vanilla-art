from django.test import TestCase
from django.urls import reverse, resolve

from artportal.about.views import about_view


class TestUrls(TestCase):
    def test_urls(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about_view)