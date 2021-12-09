from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.views import APIResponse
from user_accounts.serializers import (
    UserLoginserializer,
    UserSignupserializer
    )
from user_accounts.services import AuthServices
from core.validator import mentor_authentication


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = AuthServices.login_user(
                serializer.data["username"], 
                serializer.data["password"]
                )
            if token:
                data = {"token": token.key}
                return APIResponse(data=data, status=200, message="Success")

            return APIResponse(data={}, status=301, message="invalid username or password")

        return APIResponse(data={}, status=409, message="Invalid data")


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSignupserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = AuthServices.signup_user(
                serializer.data["username"], 
                serializer.data["password"]
                )
            if token:
                data = {"token": token.key}
                return APIResponse(data=data, status=200, message="Success")

            return APIResponse(data={}, status=301, message="user with this email already exist")

        return APIResponse(data={}, status=409, message="Invalid data")


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return APIResponse(data={}, status=200, message="Success")