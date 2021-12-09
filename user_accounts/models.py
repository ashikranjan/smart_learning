from django.db import models
from core.models import BaseModel, UserProfileManager
from django.contrib.auth.models import AbstractUser


class UserProfile(BaseModel, AbstractUser):
    id = models.AutoField(primary_key=True)
    USERTYPECHOICES = (
        ('student', 'Student'),
        ('mentor', 'Mentor')
        )
    username = None
    email = models.EmailField(max_length=255, unique=True)
    user_type = models.CharField(null=False, blank=False, max_length=50, choices=USERTYPECHOICES)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
