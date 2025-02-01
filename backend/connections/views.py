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
        

class GetAuthUserView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return Response(data={'error':'No Token. Authorization Denied'}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(id=request.user.id)
        data = UserSerializer(user).data
        return Response(data)
        
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email == "" or password == "":
            return Response({'error': 'Please provide both email and password'},status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=email, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    

class ProfileView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
           profile = request.user.profile
        except ObjectDoesNotExist:
            return Response(data={'error': "No profile found"}, status=status.HTTP_404_NOT_FOUND)
        
        profile_data = GetProfileSerializer(request.user.profile).data
        return Response(data=profile_data, status=status.HTTP_200_OK)

    def post(self, request):
        has_profile = Profile.objects.filter(user=request.user).exists()
        if has_profile:
            instance = request.user.profile
            serializer = ProfileSerializer(instance, data=request.data)
        else:
            serializer = ProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save(user=request.user)
            
            profile_data = GetProfileSerializer(request.user.profile).data
            return Response(data=profile_data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        request.user.delete()
        return Response(data={'msg': "Profile and user deleted"}, status= status.HTTP_204_NO_CONTENT)
    

class SingleProfileView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            profile_data = GetProfileSerializer(user.profile).data
            return Response(data=profile_data, status=status.HTTP_200_OK)
            
        except ObjectDoesNotExist:
            return Response(data={'error': "No profile found"}, status=status.HTTP_404_NOT_FOUND)
        

class ExperienceView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ExperienceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(profile=request.user.profile)
            profile_data = GetProfileSerializer(request.user.profile).data
            return Response(data=profile_data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, e_id):
        experience = Experience.objects.filter(profile = request.user.profile, id=e_id).first()
        if experience:
            experience.delete()
            profile_data = GetProfileSerializer(request.user.profile).data
            return Response(data=profile_data, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': "No Experience found"}, status=status.HTTP_404_NOT_FOUND)

