from django.urls import path
from .views import CoursesListView, CourseDetailView

# Creation of URL patterns for courses app

urlpatterns = [
    path("", CoursesListView.as_view(), name="courses-list"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course-details"),
]
    