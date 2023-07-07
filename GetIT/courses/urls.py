from django.urls import path
from . import views

# Creation of URL patterns for courses app

urlpatterns = [
    path("", views.courses_list, name="courses_list"),
    path("<int:pk>/", views.course_details, name="course_details"),
    path("<int:course_pk>/edit/", views.course_edit, name="course_edit"),
    path("<int:course_pk>/chapters/<int:chapter_pk>/edit/",
         views.chapter_edit, name="chapter_edit"),
    path("<int:course_pk>/lessons/<int:lesson_pk>/edit/",
         views.lesson_edit, name="lesson_edit"),
]
