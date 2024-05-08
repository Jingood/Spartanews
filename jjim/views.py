from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from accounts.models import User
from .models import Jjim
from news.models import News
from .serializers import JjimSerializer


@api_view(['POST'])
def jjim_toggle(request, news_id):
    news = get_object_or_404(News, id=news_id)
    content_type = ContentType.objects.get_for_model(news)
    try:
        Jjim.objects.get(content_type=content_type, object_id=news_id, user=request.user).delete()
        response = {
            'code': status.HTTP_200_OK,
            'message': "JJIM CANCEL SUCCESSFULLY"
        }
    except Jjim.DoesNotExist:
        Jjim.objects.create(content_type=content_type, object_id=news_id, user=request.user)
        response = {
            'code': status.HTTP_200_OK,
            "message": "JJIM SUCCESSFULLY"
        }
    return Response(response)


@api_view(['GET'])
def user_jjims(request):
    jjims = Jjim.objects.filter(user=request.user)
    serializer = JjimSerializer(jjims, many=True)
    return Response(serializer.data)
