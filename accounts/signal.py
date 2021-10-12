from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        Customer.objects.create(user=instance)
        Preferences.objects.create(user=instance)
        FamilyValues.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


def save_image_from_url(model, url):
    pass


