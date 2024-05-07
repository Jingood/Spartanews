from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    introduction = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
