from django.urls import path
from centre import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('centre/students', views.students, name='students'),
    path('centre/teachers', views.teachers, name='teachers'),
    path('centre/teachers/<str:id>', views.teacher_info, name='teacher'),
    path('centre/students/<str:id>', views.student_info, name='student')

]