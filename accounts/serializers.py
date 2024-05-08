from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from comments.serializers import CommentSerializer
from news.serializers import NewsSerializer, MyNewsSerializer
from .models import User
from news.models import News


class UserSerializer(serializers.ModelSerializer):
    my_news = SerializerMethodField()
    my_comments = SerializerMethodField()
    my_jjim_news = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'created_at',
            'introduction',
            'my_news',
            'my_comments',
            'my_jjim_news'
        ]

    def get_my_news(self, obj):
        news_queryset = obj.news.all()
        serializer = MyNewsSerializer(news_queryset, many=True)
        return serializer.data

    def get_my_comments(self, obj):
        comments_queryset = obj.comments.all()
        serializer = CommentSerializer(comments_queryset, many=True)
        return serializer.data

    def get_my_jjim_news(self, obj):
        jjim_queryset = obj.jjims.all()
        jjim_id_list = jjim_queryset.values_list('object_id', flat=True)
        news = News.objects.filter(id__in=jjim_id_list)
        serializer = MyNewsSerializer(news, many=True)
        return serializer.data
