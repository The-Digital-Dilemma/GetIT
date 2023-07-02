from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

# Create your views here.


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}

    lesson_pk = request.GET.get('lesson')
    if lesson_pk:
        context['lesson'] = get_object_or_404(Lesson, pk=lesson_pk)

    return render(request, 'courses/course_details.html', context)
