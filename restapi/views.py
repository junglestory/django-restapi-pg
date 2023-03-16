from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Board
from .serializers import BoardSerializer

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response("Hello World!")


@api_view(['GET'])
def board_list(request):
    datas = Board.objects.all()
    serializer = BoardSerializer(datas, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def board(request, board_no):
    datas = Board.objects.filter(board_no=board_no)
    serializer = BoardSerializer(datas, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def board_create(request):
    serializer = BoardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)