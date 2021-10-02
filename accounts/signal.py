from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.forms import ValidationError


@receiver(pre_save, sender=User)
def check_email(sender, instance, **kwargs):
    email = instance.email
    if sender.objects.filter(email=email).exclude(username=instance.username).exists():
        raise ValidationError('Email Already Exists')
