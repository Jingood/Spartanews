from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
