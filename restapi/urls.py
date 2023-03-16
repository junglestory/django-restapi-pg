from django.urls import path
from .views import *

urlpatterns = [
    path("hello", hello),
    path("board", board_list),
    path("board/<int:board_no>", board),
    path("board/create/", board_create),
]