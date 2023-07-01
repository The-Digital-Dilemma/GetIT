from django.urls import path
from .views import ProfileView, ProfileUpdateView, LoginInterfaceView, LogoutInterfaceView, RegisterView

app_name = 'users'  # Set the app namespace

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('login/', LoginInterfaceView.as_view(), name='login'),
    path('logout/', LogoutInterfaceView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
