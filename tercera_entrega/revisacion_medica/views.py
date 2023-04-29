from django.shortcuts import render
from revisacion_medica.models import *
from django.http import HttpResponse


def inicio(request):
    return render (request, 'revisacion_medica/inicio.html')

def cliente(request):
    return render(request, 'revisacion_medica/clientes.html')

def medico(request):
    return render(request, 'revisacion_medica/medicos.html')

def revisaciones(request):
    return render(request, 'revisacion_medica/revisacion.html')



