from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from news.models import News
from comments.models import Comment
from .models import Like

# 로그인 에러 Response
login_rquired_response = {
    'code': status.HTTP_401_UNAUTHORIZED,
    'message': 'LOGIN REQUIRED',
}


class LikeAPIView(APIView):
    def post(self, request, content_type, object_id):
        # 테스트용
        request.user = User.objects.get(username='admin')
        # 로그인 체크
        if request.user.is_authenticated:

            # 기본으로 news 모델 가져옴
            obj = get_object_or_404(News, id=object_id)
            # url에 있는 content_type 가 comment 라면 comment 모델 가져오도록 설정
            if content_type == 'comment':
                obj = get_object_or_404(Comment, id=object_id)
            # 참조할 모델 가져오기
            content_type = ContentType.objects.get_for_model(obj)

            # 해당 글에 좋아요 기록이 없을때만 데이터 추가
            if not Like.objects.filter(content_type=content_type, object_id=object_id, user=request.user).exists():
                Like.objects.create(content_type=content_type, object_id=object_id, user=request.user)
                response = {
                    'code': status.HTTP_201_CREATED,
                    'message': 'LIKED SUCCESSFULLY',
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = {
                    'code': status.HTTP_200_OK,
                    'message': 'ALREADY LIKED THIS',
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, content_type, object_id):
        # 테스트용
        request.user = User.objects.get(username='admin')
        # request.user = User.objects.get(username='adamjohnson')
        # 로그인 체크
        if request.user.is_authenticated:

            # url에 있는 content_type 가 comment 라면 comment 모델 가져오도록 설정
            obj = get_object_or_404(News, id=object_id)
            if content_type == 'comment':
                obj = get_object_or_404(Comment, id=object_id)
            # 참조할 모델 가져오기
            content_type = ContentType.objects.get_for_model(obj)
            like = Like.objects.filter(content_type=content_type, object_id=object_id, user=request.user)
            if like.exists():
                like.delete()
                response = {
                    'code': status.HTTP_204_NO_CONTENT,
                    'message': 'UNLIKED SUCCESSFULLY',
                }
                return Response(response, status=status.HTTP_204_NO_CONTENT)
            else:
                response = {
                    'code': status.HTTP_200_OK,
                    'message': 'NOT LIKED',
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(login_rquired_response, status=status.HTTP_401_UNAUTHORIZED)