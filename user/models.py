from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict


class User(AbstractUser):

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        super().save(*args, **kwargs)
