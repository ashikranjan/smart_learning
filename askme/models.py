from django.db import models
from core.models import BaseModel
from storage_backends import PublicMediaStorage
from user_accounts.models import UserProfile


class StudentQuery(BaseModel):
	id = models.AutoField(primary_key=True)
	title = models.CharField(null=False, blank=False, max_length=255)
	query = models.TextField(blank=True, null=True)
	answer = models.TextField(blank=True, null=True)
	is_closed = models.BooleanField(default=False)
	student_id = models.IntegerField(default=0)
	mentor_id = models.IntegerField(default=0)


class QueryDocuments(BaseModel):
	id = models.AutoField(primary_key=True)
	document_url = models.FileField(storage=PublicMediaStorage(), default="defaultprofilepic.png")
	query_id = models.ForeignKey(StudentQuery, on_delete=models.CASCADE)

