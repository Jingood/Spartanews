from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.URLField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news", related_query_name="news_set"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = GenericRelation('comments.Comment')
    like = GenericRelation('like.Like')

