from django.urls import path
from .views import CoursesListView, CourseDetailView, LessonDetailView

# Creation of URL patterns for courses app

urlpatterns = [
    path("", CoursesListView.as_view(), name="courses_list"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course_details"),
    path('<int:course_pk>/chapters/<int:chapter_pk>/lessons/<int:pk>/',
         LessonDetailView.as_view(), name='lesson_details'),
]
