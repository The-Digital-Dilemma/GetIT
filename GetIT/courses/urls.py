from django.urls import path
from . import views

# Creation of URL patterns for courses app

urlpatterns = [
    path("", views.courses_list, name="courses_list"),
    path("<int:pk>/", views.course_details, name="course_details"),
]
