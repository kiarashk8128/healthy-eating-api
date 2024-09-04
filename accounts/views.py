from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie
from ratelimit.decorators import ratelimit

from .serializers import CustomUserSerializer, LoginSerializer, FamilyMemberSerializer
from .models import FamilyMember


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birthday": user.birthday,
            "gender": user.gender,
            "height": user.height,
            "weight": user.weight,
            "is_family_head": user.is_family_head,
        }

        if user.is_family_head:
            family_members = user.family_members.all()
            data['family_members'] = [
                {
                    "id": member.id,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "birthday": member.birthday,
                    "gender": member.gender,
                    "height": member.height,
                    "weight": member.weight,
                }
                for member in family_members
            ]

        return Response(data)


class FamilyMembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.is_family_head:
            return Response({"detail": "User is not a family head."}, status=status.HTTP_403_FORBIDDEN)

        family_members = FamilyMember.objects.filter(family_head=user)
        serializer = FamilyMemberSerializer(family_members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@ratelimit(key='ip', rate='7/m', block=True, method='POST')
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


def health_check(request):
    return HttpResponse("OK", content_type="text/plain")
