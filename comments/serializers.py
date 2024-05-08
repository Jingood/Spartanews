from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    content_type = serializers.ReadOnlyField(source='content_type.model')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'object_id']


class CommentDetailSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'content_type',
            'content',
            'created',
            'reply',
        ]
        read_only_fields = ['author', 'object_id', 'reply']
    # 답글 목록 보기
    reply = serializers.SerializerMethodField()

    def get_reply(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        comments = Comment.objects.filter(content_type=content_type, object_id=obj.id)
        # 답글을 직렬화하여 반환
        reply_serializer = self.__class__(comments, many=True)
        return reply_serializer.data

