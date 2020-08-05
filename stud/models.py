from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
  SEMESTER_CHOICES = (
    ('1ST', 'First Semester'),
    ('2ND', 'Second Semester'),
    )
  LEVEL_CHOICES = (
    ('100', '100 Level'),
    ('200', '200 Level'),
    ('300', '300 Level'),
    ('400', '400 Level'),
    ('500', '500 Level'),
    ('600', '600 Level'),
    )
  GRADE_CHOICES = (
    (5, 'A'),
    (4, 'B'),
    (3, 'C'),
    (2, 'D'),
    (1, 'E'),
    (0, 'F'),
    )
  
  title = models.CharField(max_length = 200)
  semester = models.CharField(max_length = 4, choices = SEMESTER_CHOICES)
  level = models.CharField(max_length = 4, choices = LEVEL_CHOICES)
  grade = models.IntegerField(choices = GRADE_CHOICES)
  score = models.IntegerField()
  unit = models.IntegerField(null=True)
  course_code = models.CharField(max_length=7, null=True)
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
  
  class Meta:
    ordering = ('level',)
    
  def __str__(self):
    return self.title


#creating a cgpa models
class Level_CGPA(models.Model):
  LEVEL_CHOICES = (
    ('100', '100 Level'),
    ('200', '200 Level'),
    ('300', '300 Level'),
    ('400', '400 Level'),
    ('500', '500 Level'),
    ('600', '600 Level'),
    )
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
  first_semester_gp = models.IntegerField()
  second_semester_gp = models.IntegerField()
  cgpa = models.FloatField()
  overall_cgpa = models.FloatField()
  level = models.CharField(max_length = 4, choices = LEVEL_CHOICES)
  first_semester_unit = models.IntegerField()
  second_semester_unit = models.IntegerField()
  