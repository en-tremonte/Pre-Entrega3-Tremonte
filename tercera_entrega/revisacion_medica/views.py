from django.shortcuts import render
from revisacion_medica.models import *
from django.http import HttpResponse
from .forms import *

def inicio(request):  #funcion de vista de inicio
    return render (request, 'revisacion_medica/inicio.html')

def cliente(request): #funcion de vista de socio
    return render(request, 'revisacion_medica/clientes.html')

def medico(request): #funcion de vista de medico 
    return render(request, 'revisacion_medica/medicos.html')

def revisaciones(request): #funcion de vista de revisaciones
    return render(request, 'revisacion_medica/revisacion.html')


def clientes_form(request): #formulario de registro de socios
    if request.method == 'POST':
        formulario = Clientes_form(request.POST)
        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            cliente = clientes(nombre=informacion['nombre'], apellido=informacion['apellido'], numero_socio=informacion['numero_socio'])
            cliente.save()
            return render(request, 'revisacion_medica/inicio.html')
    else:
        formulario = Clientes_form()

    return render(request, 'revisacion_medica/clientes_form.html', {'formulario': formulario})

def medicos_form(request): #formulario de registro de medicos
    if request.method == 'POST':
        formulario = Medicos_form(request.POST)

        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            medico = medicos(nombre=informacion['nombre'], apellido=informacion['apellido'], matricula=informacion['matricula'])
            medico.save()
            return render(request, 'revisacion_medica/inicio.html')
    
    else:
        formulario = Medicos_form()
    return render(request, 'revisacion_medica/medicos_form.html', {'formulario': formulario})

def revisacion_form(request): #formulario de registro de revisaciones
    if request.method == 'POST':
        formulario = Revisaciones_form(request.POST)

        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            revisaciones = revisacion(datos_socio=informacion['datos_socio'], datos_medico=informacion['datos_medico'],fecha_revisacion=informacion['fecha_revisacion'], fecha_vencimiento=informacion['fecha_vencimiento'], apto=informacion['apto'])
            revisaciones.save()
            return render(request, 'revisacion_medica/inicio.html')
    
    else:
        formulario = Revisaciones_form()
    return render(request, 'revisacion_medica/medicos_form.html', {'formulario': formulario})

def busqueda_revisacion(request): #funcion de vista de busqueda

    return render (request, 'revisacion_medica/revisacion_search.html')

def buscar(request): #formulario de busqueda de revisaciones por nombre de socio revisado
    if request.GET['datos_socio']:

        dato_socio = request.GET['datos_socio']
        revis = revisacion.objects.filter(datos_socio__icontains=dato_socio)

        return render(request, 'revisacion_medica/resultados_search.html', {'revisaciones': revis})
    
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse (respuesta)
   

    
