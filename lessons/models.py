from django.db import models
from accounts.models import User
# Create your models here.

from datetime import datetime

from accounts.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Grade(models.Model):
    categorys = models.ManyToManyField('Category', related_name='grades')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Subject(models.Model):
    grade = models.ManyToManyField('Grade', related_name='subjects')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name="lessons")
    grade = models.ForeignKey(
        'Grade', on_delete=models.CASCADE, related_name='lessons')
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, related_name='lessons')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='lessons')

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    video = models.FileField(upload_to="videos/%Y/%m/%d/", blank=True)

    created_at = models.DateTimeField(default=datetime.now)
