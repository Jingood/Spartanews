from rest_framework import serializers
from accounts.models import User
from .models import News
from comments.serializers import CommentDetailSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    # 댓글 정보
    comments = CommentDetailSerializer(many=True, read_only=True)
    # 댓글 갯수
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ["author"]
