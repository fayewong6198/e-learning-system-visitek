from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
from .models import Category, Subject, Grade, Lesson


class Category_Grade(GenericTabularInline):
    model = Grade
    max_num = 20
    extra = 0


class Category_Admin(admin.ModelAdmin):
    inlines = [Category_Grade, ]


admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Lesson)
