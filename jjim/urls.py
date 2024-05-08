from django.urls import path
from . import views


urlpatterns = [
    path('', views.jjim_toggle, name="Jjimtoggle"),
]
