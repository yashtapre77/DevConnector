from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (
    User,
    Profile,
    Experience,
    Education,
    Post,
    Comment
)
from .utils import get_gravatar

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','avatar','date','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.avatar = get_gravatar(validated_data.get('email'))
        user.save()
        Token.objects.create(user=user)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'