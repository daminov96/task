from django.urls import path
from .views import MusicsListApiView, CategoryListApiView

urlpatterns = [
    path("musics/", MusicsListApiView.as_view()),
    path('music/category/', CategoryListApiView.as_view())
]
