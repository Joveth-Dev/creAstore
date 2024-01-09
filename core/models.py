from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # email address should be unique which is not implemented on Django by default
    email = models.EmailField(
        unique=True, help_text="Required. Please enter a valid email address."
    )
