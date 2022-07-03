from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        token['username'] = user.username
        token['password'] = user.password
        print(token)
        return token


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        print(repr(attrs))
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


# class HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = History
#         fields = ('user', 'answer', 'question')


# class AnswersSerializer(serializers.Serializer):
#     answer = serializers.CharField()
#     question_cnt = serializers.IntegerField()
#
#
# class QuestionSerializer(serializers.Serializer):
#     question = serializers.CharField()
#
#
# class HistorySerializer(serializers.Serializer):
#     user = serializers.IntegerField()
#     answer = serializers.CharField()
#     question = serializers.CharField()
