from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PersonForm

# Create your views here:
def index(request):
    professor = {"name": "John", "surname": "Dou", "age": 25}
    #template = loader.get_template('index.html')
    #dades = template.render({'nom':professor["name"], 'cognom':professor["surname"], 'edat':professor["age"]})
    #return HttpResponse(dades)
    return render(request, 'index.html', {'nom':professor["name"], 'cognom':professor["surname"], 'edat':professor["age"]})

def about(request):
    return HttpResponse("<h1>About</h1>")

alum = {
    "alum1": {
        "id": "1",
        "name": "Frederick",
        "rol": "student"
    },
    "alum2": {
        "id": "2",
        "name": "Camilo",
        "rol": "student"
    },
    "alum3": {
        "id": "3",
        "name": "Camelo",
        "rol": "student"
    }
}

prof = {
    "prof1": {
        "id": "1", 
        "name": "Roger", 
        "surname": "Sobrino", 
        "age": "39", 
        "rol": "teacher", 
        "course": "DAM2B, DAW2A"
    },
    "prof2": {
        "id": "2", 
        "name": "Oriol", 
        "surname": "Roca", 
        "age": "25", 
        "rol": "teacher", 
        "course": "DAW2B, DAW2A, DAW1A"
    },
    "prof3": {
        "id": "3", 
        "name": "Juanma", 
        "surname": "Manuel", 
        "age": "54", 
        "rol": "teacher", 
        "course": "DAW2B, DAW2A"
    }
}

def students(request):
    context = {'alums': alum}

    return render(request, 'students.html', context)
     
def teachers(request):
    
    context = {'profs': prof}

    return render(request, 'teachers.html', context)

def teacher_info(request, id):
    profesor = None
    
    for key, value in prof.items():
        if value['id'] == id:
            profesor = value
            break
        
    context = {'profs': profesor}
    return render(request, 'teacher_info.html', context)

def student_info(request, id):
    alumne = None
    
    for key, value in alum.items():
        if value['id'] == id:
            alumne = value
            break
        
    context = {'alum': alumne}
    return render(request, 'student_info.html', context)

def user_form(request): 
    form = PersonForm()
    
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {'form': form}
    return render(request, 'form.html', context)