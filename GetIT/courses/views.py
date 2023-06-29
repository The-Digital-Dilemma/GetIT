from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Course

# Create your views here.
class CoursesListView(ListView):
    model = Course
    template_name = "courses/courses-list.html"
    context_object_name = "courses-list"
    
class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course-details.html"
    context_object_name = "course-details"
    