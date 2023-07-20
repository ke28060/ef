from django.shortcuts import render, HttpResponse,redirect
from miapp.models import pais
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def pais(request):
    pais = Pais.objects.all()
    """cursos=Curso.object.filter(
        Q(nombre__contains="Py") |
        Q(nombre__contains="Hab")
        )"""
    return render(request,'pais.html',{
        'pais':pais,
        'nombre': 'Listado de pais'
    })
def eliminar_pais(request, id):
    pais = Pais.objects.get(pk=id)
    pais.delete()
    return redirect('Pais')
def buscar_pais(request, id):
    try:
        pais = Pais.objects.get(id=1000)
        resultado = f"""Pais:
                    <br> <strong>ID:</strong> {pais.id}
                    <br> <strong>Nombre: </strong> {pais.nombre}
                    <br> <strong>poblacion: </strong> {pais.poblacion}
        """
    except:
        resultado = "<h1> curso no encontrado</h1>"
    return HttpResponse(resultado)
def Crear_pais(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        poblacion = request.POST['poblacion']
        estado = request.POST['estado'] == 'En curso'
        
        pais = Pais(
            codigo = codigo,
            nombre = nombre,
            poblacion = poblacion,
            estado = estado
        )
        pais.save()
        messages.success(request, f'se agrago correctamente el curso: {pais.nombre}')
        return redirect('Pais')
    else:
        return HttpResponse("<h2>nos e puedo guardar</h2>")
def editoriales(request):
    return render(request, 'editoriales.html')
def CrearEditorial(request):
    return render(request, 'creareditoriales.html')
def Crearpais(request):
    return render(request, 'registrarpaises.html')