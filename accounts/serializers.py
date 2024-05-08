from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from comments.serializers import CommentSerializer
from news.serializers import NewsSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    my_news = SerializerMethodField()
    my_comments = SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'created_at', 'introduction', 'my_news', 'my_comments']

    def get_my_news(self, obj):
        news_queryset = obj.news.all()
        serializer = NewsSerializer(news_queryset, many=True)
        return serializer.data

    def get_my_comments(self, obj):
        comments_queryset = obj.comments.all()
        serializer = CommentSerializer(comments_queryset, many=True)
        return serializer.data
