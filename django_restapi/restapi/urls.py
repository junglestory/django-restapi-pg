from django.urls import path
from .views import *

urlpatterns = [
    path("hello/", hello),
    path("board/", board),
    path("board/<str:board_no>/", board_list),
    path("board/create", board_create),
]