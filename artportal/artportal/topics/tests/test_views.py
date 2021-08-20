from django.test import TestCase, Client
from django.urls import reverse


# class TopicTypeTest(TestCase):
#     def test_topic_type_view_GET(self):
#         client = Client()
#         response = client.get(reverse('topics'))
#         # self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'topics.html')


class TopicTypeGraphicViewTest(TestCase):
    def test_topic_type_graphic_view_GET(self):
        client = Client()
        response = client.get(reverse('more topic graphic'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/sections/topic-sections-graphic.html')


class TopicTypePhotographyViewTest(TestCase):
    def test_topic_type_photography_view_GET(self):
        client = Client()
        response = client.get(reverse('more topic photography'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/sections/topic-sections-photography.html')

class TopicTypeFineArtTest(TestCase):
    def test_topic_type_fine_art_view_GET(self):
        client = Client()
        response = client.get(reverse('more topic fine art'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/sections/topic-sections-fine-art.html')

class TopicTypeJewelleryViewTest(TestCase):
    def test_topic_type_jewellery_view_GET(self):
        client = Client()
        response = client.get(reverse('more topic jewellery'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/sections/topic-sections-jewellery.html')

class TopicTypeOtherViewTest(TestCase):
    def test_topic_type_other_view_GET(self):
        client = Client()
        response = client.get(reverse('more topic other'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'topics/sections/topic-sections-other.html')