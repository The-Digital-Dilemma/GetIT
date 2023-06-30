from django.urls import path
from .views import ProfileView

app_name = 'users'  # Set the app namespace

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
]