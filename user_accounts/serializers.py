import re
from rest_framework import serializers, exceptions


class UserLoginserializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=30)


class UserSignupserializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=30)