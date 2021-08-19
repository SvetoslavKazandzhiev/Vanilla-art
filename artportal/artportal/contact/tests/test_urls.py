from django.test import TestCase
from django.urls import reverse, resolve

from artportal.contact.views import contact_view


class TestContactUrls(TestCase):
    def test_contact_urls(self):
        url = reverse('contact view')
        self.assertEqual(resolve(url).func, contact_view)