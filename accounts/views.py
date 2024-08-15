from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny


@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
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


@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'birthday': user.birthday,
            'gender': user.gender,
            'height': user.height,
            'weight': user.weight,
            'is_family_head': user.is_family_head
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ensure_csrf_cookie
def homepage(request):
    return HttpResponse("Welcome to the Homepage!")
