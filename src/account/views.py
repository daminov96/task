from django.shortcuts import render
from drf_yasg import openapi
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework import status as rest_status
from .serializers import RegisterSerializer, TokenSerializer
from rest_framework_simplejwt.views import (TokenObtainPairView as JWTTokenObtainPairView,
                                            TokenRefreshView as JWTTokenRefreshView,
                                            )
from rest_framework.response import Response


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class TokenGenerateView(JWTTokenObtainPairView):
    serializer_class = TokenSerializer
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description='Token obtained'),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description='User not found'),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(description='Validation error'),
    }

    def get_serializer_context(self):
        return {'request': self.request}


class TokenRefreshView(JWTTokenRefreshView):
    post_responses = {
        rest_status.HTTP_201_CREATED: openapi.Response(description='Token obtained'),
        rest_status.HTTP_404_NOT_FOUND: openapi.Response(description='Token not found'),
        rest_status.HTTP_400_BAD_REQUEST: openapi.Response(description='Validation error'),
    }
