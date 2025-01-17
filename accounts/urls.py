from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView


urlpatterns = [
    path('signup/', views.UserSignupAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]