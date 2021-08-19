from django.urls import reverse

from artportal.art_app.models import Art
from tests.base.mixins import ArtTestUtils, UserTestUtils
from tests.base.tests import ArtportalTestCase


class ArtDetailsTest(ArtTestUtils, UserTestUtils, ArtportalTestCase):
    def test_getArtDetails_whenArtDoesnotexistAndis_owner_return_detailsforOwner(self):
        self.client.force_login(self.user)
        art = self.create_art(
            name='Test name',
            description='Test description',
            image='path/to/image.png',
            type=Art.PHOTOGRAPHY,
            user=self.user,
        )

        response = self.client.get(reverse('details art img', kwargs={
            'pk': art.id,
        }))

        self.assertTrue(response.context['is_owner'])

    def test_getArtDetails_whenArtexistAndis_owner_return_detailsforOwner(self):
        self.client.force_login(self.user)
        art = self.create_art(
            name='Test name',
            description='Test description',
            image='path/to/image.png',
            type=Art.PHOTOGRAPHY,
            user=self.user,
        )

        response = self.client.get(reverse('details art img', kwargs={
            'pk': art.id,
        }))

        self.assertTrue(response.context['is_owner'])