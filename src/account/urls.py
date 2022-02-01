from django.urls import path
from .views import RegisterView, TokenRefreshView, TokenGenerateView

urlpatterns = [
    path("sign-up/", RegisterView.as_view()),
    path('login/', TokenGenerateView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
