from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from user_accounts.models import UserProfile


class AuthServices:
    @classmethod
    def login_user(self, email, password):
        try:
            user = authenticate(email=email, password=password)
            token, is_created= Token.objects.get_or_create(user=user)
            return token
        except Exception as e:
            return False

    @classmethod
    def signup_user(self, email, password):
        try:
            user = UserProfile.objects.create_user(email=email, password=password)
            user.user_type='student'
            user.save()
            token, is_created= Token.objects.get_or_create(user=user)
            return token
        except Exception as e:
            print(e)
            return False

