from django.urls import path
from . import views


urlpatterns = [
    path('news/<int:news_id>/', views.jjim_toggle, name="Jjimtoggle"),
]
