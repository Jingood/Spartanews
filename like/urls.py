from django.urls import path
from .views import LikeAPIView

urlpatterns = [
    # content_type : news / comment 구분
    # object_id : news_id / comment_id 구분
    path('<str:content_type>/<int:object_id>/', LikeAPIView.as_view())
]