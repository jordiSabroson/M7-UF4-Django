from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here:
def index(request):
    professor = {"name": "John", "surname": "Dou", "age": 25}
    #template = loader.get_template('index.html')
    #dades = template.render({'nom':professor["name"], 'cognom':professor["surname"], 'edat':professor["age"]})
    #return HttpResponse(dades)
    return render(request, 'index.html', {'nom':professor["name"], 'cognom':professor["surname"], 'edat':professor["age"]})

def about(request):
    return HttpResponse("<h1>About</h1>")


