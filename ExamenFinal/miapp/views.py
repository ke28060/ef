from django.shortcuts import render, HttpResponse,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def pais(request):
    return render(request,'pais.html')
def Crearpais(request):
    return render(request,'registrarpaises.html')
def editoriales(request):
    return render(request, 'editoriales.html')
def CrearEditorial(request):
    return render(request, 'creareditoriales.html')

