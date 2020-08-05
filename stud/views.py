from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Course, Level_CGPA
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
  lis = Course.objects.all().filter(user__username = request.user.username).order_by("-level")
  
  #getting the unique levels, i didnt want to create a new model for levels so i compromised
  cgpa = 0
  level_set = set()
  for l in lis:
    level_set.add(l.level)
  try:
    cgpa = getting_gp(lis, lis)/summing_unit(lis)
    
  except:
    pass
  
  context = {"level" : list(level_set), "cgpa": cgpa}
  
  return render(request, 'base.html', context)

@login_required
def course_list(request, lev):
    
    lis = Course.objects.all().filter(user__username = request.user.username).order_by("-level").filter(level=lev)
    cgpa = getting_gp(lis, lis)/summing_unit(lis)
    context = {'1st': Course.objects.all().filter(user__username = request.user.username).filter(level=lev).filter(semester="1ST"),
      '2nd': Course.objects.all().filter(user__username = request.user.username).filter(level = lev).filter(semester="2ND"),
      'cgpa': cgpa,
      
    }
    return render(request, 'stud/course_list.html', context)

@login_required
def delete(request, course_id):
  course = Course.objects.get(id=course_id)
  course.delete()
  lis = Course.objects.all().filter(user__username = request.user.username).order_by("-level")
  
  #getting the unique levels, i didnt want to create a new model for levels so i compromised
  cgpa = 0
  level_set = set()
  for l in lis:
    level_set.add(l.level)
  try:
    cgpa = getting_gp(lis, lis)/summing_unit(lis)
    
  except:
    pass
  
  context = {"level" : list(level_set), "cgpa": cgpa}
  
  return render(request, 'base.html', context)

    
class CourseDetail(DetailView):
  model = Course 
  context_object_name = 'course'

  def get_queryset(self):
    return Course.objects.filter()
        
  
def summing_unit(i):
    
    return sum([x.unit for x in i])
    
def getting_gp(unit1, unit2):
  return sum([i.unit * j.grade for i, j in zip(unit1, unit2)])
  
from django.http import HttpResponseRedirect 
from .forms import CourseForm 


@login_required
def course_req(request):
  submitted = False 
  if request.method == 'POST':
    form = CourseForm(request.POST) 
    
    if form.is_valid():
      new_form = form.save(commit=False) 
      new_form.user = request.user
      new_form.save()
      return HttpResponseRedirect('/create/?submitted=True') 
  else:
    form = CourseForm() 
    if'submitted' in request.GET:
      submitted = True 
  return render(request, 'stud/course.html', {'form': form, 'submitted': submitted})
  
  
@login_required 
def course_edit(request, course_id):
  course = Course.objects.get(id=course_id)
  submitted = False 
  if request.method == 'POST':
    form = CourseForm(instance = course, data = request.POST) 
    if form.is_valid():
      form.save() 
      #return HttpResponseRedirect('/edit/course_id?submitted=True') 
  else:
    form = CourseForm(instance = course) 
    if'submitted' in request.GET:
      submitted = True 
  return render(request, 'stud/edit.html', {'form': form, 'submitted': submitted})
  
  
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy # ...

class Register(CreateView):
  template_name = 'registration/register.html' 
  form_class = UserCreationForm 
  success_url = reverse_lazy('register-success') 
  def form_valid(self, form):
    form.save() 
    return HttpResponseRedirect(self.success_url)