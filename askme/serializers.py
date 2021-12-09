import re
from rest_framework import serializers, exceptions


class StudentQueryserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student_id = serializers.IntegerField()
    mentor_id = serializers.IntegerField()
    title = serializers.CharField()
    desc = serializers.CharField()
    answer = serializers.CharField(read_only=True)