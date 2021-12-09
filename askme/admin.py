from django.contrib import admin
from askme.models import StudentQuery
from user_accounts.models import UserProfile


class StudentQueryAdmin(admin.ModelAdmin):
    model = StudentQuery
    list_display = ['title', 'student', 'mentor']

    def student(self, obj):
        return UserProfile.objects.filter(id=obj.student_id).first().email 

    def mentor(self, obj):
        return UserProfile.objects.filter(id=obj.mentor_id).first().email 

admin.site.register(StudentQuery, StudentQueryAdmin)

