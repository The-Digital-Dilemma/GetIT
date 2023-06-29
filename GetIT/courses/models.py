from django.db import models
from django.urls import reverse

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Choose a programming language from the list
    language = [
        ('Visual Basic .NET', 'Visual Basic .NET'),
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('HTML/CSS', 'HTML/CSS'),
    ]
    language = models.CharField(max_length=20, choices=language)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course-details", kwargs={"pk": self.pk})
    

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Use chapter number for ordering
    chapter_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['chapter_number']

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    # Use lesson number for ordering
    lesson_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        ordering = ['lesson_number']

    def __str__(self):
        return self.title
    