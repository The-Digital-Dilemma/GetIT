from django.contrib import admin
from .models import Course, Chapter, Lesson

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    list_filter = ('language',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_number', 'title', 'course')
    list_filter = ('course',)
    ordering = ('course', 'chapter_number')
    list_display_links = ('chapter_number', 'title',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'title', 'chapter')
    list_filter = ('chapter',)
    ordering = ('lesson_number',)
    list_display_links = ('lesson_number', 'title',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson, LessonAdmin)
