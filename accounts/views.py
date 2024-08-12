from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birthday': user.birthday,
            'gender': user.gender,
            'height': user.height,
            'weight': user.weight,
            'is_family_head': user.is_family_head
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def homepage(request):
    return HttpResponse("Welcome to the Homepage!")
