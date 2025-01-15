import json
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status

from .models import Avatar, Profile
from .serializers import ProfileSerializer


@api_view(['GET', 'POST'])
def sign_in(request: Request) -> Response:
    if request.method == 'POST':
        user_data = json.loads(request.body)
        username = user_data.get('username')
        password = user_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sign_out(request: Request) -> Response:
    if request.method == 'POST':
        logout(request)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def sign_up(request: Request) -> Response:
    if request.method == 'POST':
        user_data = json.loads(request.body)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")

        try:
            avatar = Avatar.objects.filter(pk=1).first()
            if avatar is None:
                avatar = Avatar.objects.create(src="/avatars/default.jpeg", alt='default')
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user, fullName=name, avatar=avatar)

            if user is not None:
                login(request, user)

            return Response(status=status.HTTP_200_OK)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_profile(request: Request) -> Response:
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            user_data = request.data
            fullName = user_data.get("fullName")
            email = user_data.get("email")
            phone = user_data.get("phone")
            Profile.objects.filter(user=request.user).update(fullName=fullName, email=email, phone=phone)

            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(profile)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_password(request: Request) -> Response:
    if request.method == 'POST':
        current_password = request.data.get('currentPassword')
        new_password = request.data.get('newPassword')
        user = User.objects.get(username=request.user)

        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()

        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])
def user_avatar(request: Request) -> Response:
    if request.method == 'POST':
        file = request.FILES["avatar"]
        fs = FileSystemStorage()
        name = os.path.join(settings.MEDIA_ROOT, 'avatars', request.user.username, file.name)
        avatar = Avatar.objects.create(src=os.path.join('avatars', request.user.username, file.name),
                                       alt=request.user.username + file.name)
        Profile.objects.filter(user=request.user).update(avatar=avatar)
        fs.save(name=name, content=file)

    return Response(status=status.HTTP_200_OK)
