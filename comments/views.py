from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.views import APIView
from accounts.models import User
from .models import Comment
from news.models import News
from rest_framework.response import Response
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class NewsCommentAPIView(APIView):

    def get(self, request, news_id):
        news = get_object_or_404(News, id=news_id)
        content_type = ContentType.objects.get_for_model(news)
        comments = Comment.objects.filter(content_type=content_type, object_id=news_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        # 임시용
        user = User.objects.get(username='admin')
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=user, content_object=news)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentReplyAPIView(APIView):

    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        content_type = ContentType.objects.get_for_model(comment)
        comments = Comment.objects.filter(content_type=content_type, object_id=comment_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        print(comment)
        # 임시용
        user = User.objects.get(username='admin')
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=user, content_object=comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
