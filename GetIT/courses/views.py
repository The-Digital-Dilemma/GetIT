from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView


from .models import Course, Lesson

# Create your views here.


class CoursesListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"
    context_object_name = "courses"


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_details.html"
    context_object_name = "course"


class LessonDetailView(DetailView):
    model = Lesson
    template_name = "courses/lesson_details.html"
    context_object_name = "lesson"

    def get_object(self):
        return get_object_or_404(Lesson, chapter__course__pk=self.kwargs['course_pk'], chapter__pk=self.kwargs['chapter_pk'], pk=self.kwargs['pk'])
