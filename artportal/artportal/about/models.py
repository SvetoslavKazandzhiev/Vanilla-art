from django.db import models


class About(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
    )
    description = models.TextField(
        max_length=200,
        blank=True,
    )
    image = models.ImageField(
        upload_to='media'
    )
    def __str__(self):
        return self.name