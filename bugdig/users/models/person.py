from django.db import models
from django.contrib.auth.models import User

class Person(User):
    """
    # Person
    Proxy for default django User model.

    Implements additional methods.

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

    class Meta:
        proxy = True

