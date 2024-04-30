from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UsuariForm
from . import models


# Create your views here:
def index(request):
    return render()


def students(request):
    rol = 2
    students = models.Usuari.objects.get(rol_id=rol)
    context = {"student": students}
    return render(request, "students.html", context)


def teachers(request):

    return render(request, "teachers.html")


def teacher_info(request, id):
    profesor = None

    for key, value in prof.items():
        if value["id"] == id:
            profesor = value
            break

    context = {"profs": profesor}
    return render(request, "teacher_info.html", context)


def student_info(request, id):
    alumne = None

    for key, value in alum.items():
        if value["id"] == id:
            alumne = value
            break

    context = {"alum": alumne}
    return render(request, "student_info.html", context)


def user_form(request):
    form = UsuariForm()

    if request.method == "POST":
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UsuariForm()

    context = {"form": form}
    return render(request, "form.html", context)
