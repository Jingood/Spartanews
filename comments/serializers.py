from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    content_type = serializers.ReadOnlyField(source='content_type.model')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'object_id']


