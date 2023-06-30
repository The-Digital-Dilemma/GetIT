from django.urls import path
from .views import ProfileView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    #other urls for the update of the profile
]