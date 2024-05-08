from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Jjim
from .serializers import JjimSerializer


@api_view(['POST'])
def jjim_toggle(request, content_type_slug, object_id):
    try:
        content_type = get_object_or_404(content_type, slug=content_type_slug)
        content_object = get_object_or_404(
            content_type.model_class(), pk=object_id)
    except (content_type.DoesNotExist, content_type.model_class().DoesNotExist):
        return Response({'error': 'Invalid content type or object'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        jjim = Jjim.objects.get(content_type=content_type,
                                object_id=object_id, user=request.user)
        jjim.delete()
        is_liked = False
    except Jjim.DoesNotExist:
        jjim = Jjim.objects.create(
            content_type=content_type, object_id=object_id, user=request.user)
        is_liked = True

    serializer = JjimSerializer(jjim)
    return Response(serializer.data)


@api_view(['GET'])
def user_jjims(request):
    jjims = Jjim.objects.filter(user=request.user)
    serializer = JjimSerializer(jjims, many=True)
    return Response(serializer.data)
