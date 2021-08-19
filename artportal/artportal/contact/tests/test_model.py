from django.test import TestCase
from artportal.contact.models import Contact


class TestModel(TestCase):
    def test_contact_Model(self):
        obj = Contact.objects.create(
            email='qwe@aa.com',
            subject='test',
            message='hi',
        )
        obj.save()
        self.assertEqual(obj.email, 'qwe@aa.com')
        self.assertEqual(obj.subject, 'test')
        self.assertEqual(obj.message, 'hi')

