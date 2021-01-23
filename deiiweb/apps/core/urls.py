from django.urls import path
from .views import HomePageView, UserListView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('usuarios/', UserListView.as_view(), name="usuarios"),
]