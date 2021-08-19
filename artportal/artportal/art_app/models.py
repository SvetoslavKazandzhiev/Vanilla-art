from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Art(models.Model):
    JEWELLERY = 'jewellery'
    GRAPHIC = 'graphic'
    PHOTOGRAPHY = 'photography'
    FINE_ART = 'fine art'
    OTHER = 'other'
    DESIGN_TYPES = (
        (JEWELLERY, 'jewellery'),
        (GRAPHIC, 'graphic'),
        (PHOTOGRAPHY, 'photography'),
        (FINE_ART, 'fine art'),
        (OTHER, 'other'),
    )
    type = models.CharField(
        max_length=15,
        choices=DESIGN_TYPES,
        default=OTHER,
    )
    name = models.CharField(
        max_length=20,
    )
    description = models.TextField(
        max_length=200,
    )
    image = models.ImageField(
        upload_to='media'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}, {self.description}, {self.image}'


class Comment(models.Model):
    text = models.TextField()
    art = models.ForeignKey(
        Art,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )