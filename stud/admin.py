from django.contrib import admin
from .models import Course
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ('course_code', 'semester', 'grade', 'unit')
  list_filter = ('level', 'semester')
  