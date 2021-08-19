from django.db import models


class Topics(models.Model):
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
    name = models.CharField(max_length=50)
    topic_type = models.CharField(max_length=25, choices=DESIGN_TYPES, default=OTHER)
    description = models.TextField()
    image = models.ImageField(
        upload_to='media'
    )