from django import forms
from .models import Course, Chapter, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'language')


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('course', 'chapter_number', 'title')


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('chapter', 'lesson_number', 'title', 'content')
