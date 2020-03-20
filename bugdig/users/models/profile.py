from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .person import Person

class Profile ( models.Model ):
    """
    # Profile
    Additional fields for Persons can be added here.
    """

    user = models.OneToOneField(Person, on_delete=models.CASCADE)

    location = models.CharField(max_length=30, blank=True)

    date_birth = models.DateField(null=True, blank=True)

@receiver(post_save, sender=Person)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Person)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
