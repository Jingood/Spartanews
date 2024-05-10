from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.views import APIView
from accounts.models import User
from .models import Comment
from news.models import News
from rest_framework.response import Response
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404

# 로그인 에러 Response
login_rquired_response = {
    'code': status.HTTP_401_UNAUTHORIZED,
    'message': 'LOGIN REQUIRED',
}

# 권한 에러 Response
permission_denied_response = {
    'code': status.HTTP_403_FORBIDDEN,
    'message': 'Permission denied.'
}


# Create your views here.
class NewsCommentAPIView(APIView):

    # 뉴스 댓글 목록
    def get(self, request, news_id):
        news = get_object_or_404(News, id=news_id)
        print(news.comments)
        # 참조하는 모델 가져오기
        content_type = ContentType.objects.get_for_model(news)
        # 참조하는 모델 AND PK 조회
        comments = Comment.objects.filter(content_type=content_type, object_id=news_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 뉴스 댓글 등록
    def post(self, request, news_id):
        # 로그인 체크
        if request.user.is_authenticated:
            news = News.objects.get(id=news_id)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user, content_object=news)
                response = {
                    'code': status.HTTP_201_CREATED,
                    'message': 'COMMENT CREATED SUCCESSFULLY',
                    'data': serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)


class CommentReplyAPIView(APIView):

    # 댓글 리플 목록
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        # 참조하는 모델 가져오기
        content_type = ContentType.objects.get_for_model(comment)
        # 참조하는 모델 AND PK 조회
        comments = Comment.objects.filter(content_type=content_type, object_id=comment_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 댓글 리플 등록
    def post(self, request, comment_id):
        if request.user.is_authenticated:
            comment = get_object_or_404(Comment, id=comment_id)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user, content_object=comment)
                response = {
                    'code': status.HTTP_201_CREATED,
                    'message': 'COMMENT CREATED SUCCESSFULLY',
                    'data': serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)


class CommentAPIView(APIView):

    # 댓글 수정
    def put(self, request, comment_id):
        # 로그인 체크
        if request.user.is_authenticated:
            comment = get_object_or_404(Comment, id=comment_id)
            # 작성자 체크
            if request.user != comment.author:
                return Response(permission_denied_response, status=status.HTTP_403_FORBIDDEN)

            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                    'code': status.HTTP_200_OK,
                    'message': 'COMMENT UPDATED SUCCESSFULLY',
                    'data': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)

    # 댓글 삭제
    def delete(self, request, comment_id):
        # 로그인 체크
        if request.user.is_authenticated:
            comment = get_object_or_404(Comment, id=comment_id)
            # 작성자 체크
            if request.user != comment.author:
                return Response(permission_denied_response, status=status.HTTP_403_FORBIDDEN)

            comment.delete()
            response = {
                'code': status.HTTP_200_OK,
                'message': 'COMMENT DELETED SUCCESSFULLY'
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)