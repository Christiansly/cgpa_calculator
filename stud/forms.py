from django import forms 
from django.forms import ModelForm 
from .models import Course
class CourseForm(ModelForm):
  required_css_class = 'required' 
  class Meta:
    model = Course
    fields = ['title', 'semester', 'level', 'grade', 'score', 'unit', 'course_code']
    
class CourseEdit(ModelForm):
  class Meta:
    model = Course 
    fields = ['title', 'semester', 'level', 'grade', 'score', 'unit', 'course_code']