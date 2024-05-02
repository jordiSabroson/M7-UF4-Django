from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import UsuariForm
from . import models


# Create your views here:
def index(request):
    total_users = models.Usuari.objects.count()
    context = {"total_users": total_users}
    return render(request, "index.html", context)


def students(request):
    students = models.Usuari.objects.filter(rol_id=2)
    context = {"students": students}
    return render(request, "students.html", context)


def teachers(request):
    teachers = models.Usuari.objects.filter(rol_id=1)
    context = {"teachers": teachers}
    return render(request, "teachers.html", context)


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


def update(request, id):
    user = models.Usuari.objects.get(id=id)
    form = UsuariForm(instance=user)

    if request.method == "POST":
        form = UsuariForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "update.html", context)


def delete(request, id):
    user = get_object_or_404(models.Usuari, id=id)
    if request.method == "POST":
        user.delete()
        return redirect("index")
    context = {"user": user}
    return render(request, "delete.html", context)
