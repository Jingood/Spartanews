from django.urls import path
from .views import NewsCommentAPIView, CommentReplyAPIView, CommentAPIView

urlpatterns = [
    # 뉴스 댓글
    path('news/<int:news_id>/', NewsCommentAPIView.as_view()),
    # 댓글 리플
    path('reply/<int:comment_id>/', CommentReplyAPIView.as_view()),
    # 댓글 수정/삭제
    path('<int:comment_id>/', CommentAPIView.as_view()),
]