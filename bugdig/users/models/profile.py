from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

class Profile ( models.Model ):
    """
    # Profile
    It's purpose is to extend the django User model.

    User model fields:
    - username
    - first_name
    - last_name
    - email
    - password
    - groups
    - user_permissions
    - is_staff
    - is_active
    - is_superuser
    - last_login
    - date_joined

    Django Users Docs:

    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User
    """

    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30, blank=True)

    date_birth = models.DateField(null=True, blank=True)

    def __str__(self ):
        return f"{self.user.username}"

    def __repr__(self ):
        return f"{self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
