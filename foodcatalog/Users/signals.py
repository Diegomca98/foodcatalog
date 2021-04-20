from django.db.models.signals import post_save # Send signal when save()
from django.contrib.auth.models import User
from django.dispatch import receiver # Receive signal from post_save
from .models import Profile

#The instance is the user that's being created
#Created is a bool value and holds the status of creation of the user

@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()