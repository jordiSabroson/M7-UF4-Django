from django.urls import path
from centre import views

urlpatterns = [
    path("", views.index, name="index"),
    path("centre/students", views.students, name="students"),
    path("centre/teachers", views.teachers, name="teachers"),
    path("form/", views.user_form, name="form"),
    path("update/<str:id>", views.update, name="update"),
    path("delete/<str:id>", views.delete, name="delete"),
]
