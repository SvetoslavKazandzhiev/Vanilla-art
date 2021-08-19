from django.contrib.auth import get_user_model

from artportal.art_app.models import Art


UserModel = get_user_model()

class ArtTestUtils:
    def create_art(self, **kwargs):
        return Art.objects.create(**kwargs)


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)