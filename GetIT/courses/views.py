from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Chapter, Lesson
from .forms import CourseForm, ChapterForm, LessonForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def courses_list(request):
    courses = Course.objects.all()
    user_is_admin_or_instructor = False
    if request.user.groups.filter(name__in=['Administrator', 'Instructor']).exists():
        user_is_admin_or_instructor = True
    context = {'courses': courses,
               'user_is_admin_or_instructor': user_is_admin_or_instructor}
    return render(request, 'courses/courses_list.html', context)


@login_required(login_url='/users/login/')
def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user_is_admin_or_instructor = False
    if request.user.groups.filter(name__in=['Administrator', 'Instructor']).exists():
        user_is_admin_or_instructor = True
    context = {'course': course,
               'user_is_admin_or_instructor': user_is_admin_or_instructor}

    lesson_pk = request.GET.get('lesson')
    if lesson_pk:
        context['lesson'] = get_object_or_404(Lesson, pk=lesson_pk)
        context['chapter'] = context['lesson'].chapter

    return render(request, 'courses/course_details.html', context)


def course_edit(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('courses_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})


def chapter_edit(request, course_pk, chapter_pk):
    chapter = get_object_or_404(Chapter, pk=chapter_pk)
    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.save()
            return redirect('course_details', pk=course_pk)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'courses/chapter_edit.html', {'form': form})


def lesson_edit(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            return redirect('course_details', pk=course_pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'courses/lesson_edit.html', {'form': form})
