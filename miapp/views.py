from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Pais
from miapp.models import editorial
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
    return render(request,'Pais.html',{
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
    editoriale = editorial.objects.all()
    """editoriale=Editorial.object.filter(
        Q(nombre__contains="Py") |
        Q(nombre__contains="Hab")
        )"""
    return render(request,'editoriales.html',{
        'editoriale':editoriale,
        'nombre': 'Listado de editoriale'
    })

def crear_editorial(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        url = request.POST['url']
        imagen = request.FILES.get('imagen')
        estado =request.POST['estado'] == 'En curso'

        editorial.objects.create(nombre=nombre, url=url, imagen=imagen, estado=estado)
        messages.success(request, 'La editorial se registró correctamente.')
    else:
        return HttpResponse("<h2>nos e puedo guardar</h2>")
    return render(request, 'editoriales.html')

def eliminar_editorial(request, id_editorial):
    editorial = editorial.objects.get(pk=id_editorial)
    editorial.delete()
    messages.success(request, 'La editorial se eliminó correctamente.')
    return redirect('editoriales')
def Crearpais(request):
    return render(request, 'registrarpaises.html')
def creareditorial(request):
    return render(request, 'creareditoriales.html')


