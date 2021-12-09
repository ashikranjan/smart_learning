from user_accounts.views import (
    RegisterView, 
    LoginView, 
    LogoutView)
from django.urls import path

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', RegisterView.as_view())
]
