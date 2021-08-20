from django.test import TestCase

from artportal.contact.forms import ContactForm


class TestContactForm(TestCase):
    def test_contact_form_wit_data(self):
        obj = ContactForm(data={
            'email':'qwe@aa.com',
            'subject': 'test',
           'message': 'hi',
        }
        )

        self.assertTrue(obj.is_valid())

    def test_contact_form_without_data(self):
        obj = ContactForm(data={})

        self.assertFalse(obj.is_valid())
        self.assertEquals(len(obj.errors), 3)