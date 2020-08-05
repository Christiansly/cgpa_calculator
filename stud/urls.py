from django.urls import path
from . import views
from .views import CourseDetail
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.course_req, name='create'),
    path('level/<str:lev>', views.course_list, name='course-list'),
    path('level/courses/<int:pk>', CourseDetail.as_view(), name='course-detail'),
    path('level/courses/edit/<int:course_id>', views.course_edit, name = 'edit'),
    path('level/course/delete/<int:course_id>', views.delete, name='delete'),
  ]