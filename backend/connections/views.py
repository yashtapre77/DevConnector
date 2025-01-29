from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.conf import settings
import requests

from .serializers import (
    UserSerializer,
    ProfileSerializer,
    GetProfileSerializer,
    ExperienceSerializer,
    EducationSerializer,
    PostSerializer,
    GetPostSerializer,
    CommentSerializer
)
from .models import (
    User,
    Profile,
    Experience,
    Education,
    Post,
    Comment
)

# Create your views here.

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get(user_id=serializer.data.get('id'))
            return Response(data={'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
