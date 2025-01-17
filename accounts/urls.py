from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
]