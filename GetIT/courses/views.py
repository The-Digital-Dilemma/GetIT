from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Course

# Create your views here.
class CoursesListView(ListView):
    model = Course
    template_name = "courses.html"
    context_object_name = "courses"
    
class CourseDetailView(DetailView):
    model = Course
    template_name = "course.html"
    context_object_name = "course"
    