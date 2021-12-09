import json
from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from core.views import APIResponse
from askme.serializers import StudentQueryserializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from askme.models import StudentQuery, QueryDocuments
from core.validator import mentor_authentication, student_authentication
from utilities.aws_manager import AWSManager
from utilities.send_email import GoogleSendEmailManager


aws_manager = AWSManager()
email_manager = GoogleSendEmailManager()


class SubmitQueryView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if not student_authentication(request.user):
            return APIResponse(data={}, status=403, message="only student can submit query")

        serializer = StudentQueryserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            query = StudentQuery(**request.data)
            query.save()
            return APIResponse(data={}, status=200, message="Success")
            
        return APIResponse(data={}, status=409, message="Invalid data")


class AnswerQueryView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, query_id):
        if not mentor_authentication(request.user):
            return APIResponse(data={}, status=403, message="only mentor can answer query")

        query = StudentQuery.objects.filter(id=query_id, mentor_id=request.user.id).first()
        if not query:
            return APIResponse(data={}, status=404, message="no query found")

        query.answer = request.data.get('answer')
        query.save()

        student_email = UserProfile.objects.filter(id=query.student_id).first().email
        email_manager.google_send_email("Subject", "text", settings.EMAIL_HOST_USER, [student_email])
        
        return APIResponse(data={}, status=200, message="Success")


class UploadQueryDocumentView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, query_id):
        if not student_authentication(request.user):
            return APIResponse(data={}, status=403, message="only student can upload query documents")

        query = StudentQuery.objects.filter(id=query_id).first()
        if not query:
            return APIResponse(data={}, status=404, message="no query found")

        file_obj = request.FILES.get('file')
        if not file_obj:
            return APIResponse(data={}, status=404, message="please slect the file")

        uploaded = aws_manager.upload_file_to_s3(file_obj)
        if not uploaded:
            return APIResponse(data={}, status=409, message="file upload failed please try again later")

        document = QueryDocuments(query_id=query.id, document_url=uploaded)
        document.save()
        return APIResponse(data={}, status=200, message="Success")


