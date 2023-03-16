from django.urls import path
from .views import *

urlpatterns = [
    path("hello/", hello),
    path("board/create/", board_create),
]