from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from artportal.art_auth.models import Account

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        account = Account(
            user=instance,
        )
        account.save()