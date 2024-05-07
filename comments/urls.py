from django.urls import path
from .views import NewsCommentAPIView, CommentReplyAPIView


urlpatterns = [
    path('<int:comment_id>/', CommentReplyAPIView.as_view()),
    path('news/<int:news_id>/', NewsCommentAPIView.as_view()),

]