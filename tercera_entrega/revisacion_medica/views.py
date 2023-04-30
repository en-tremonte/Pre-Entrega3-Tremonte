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

def clientes_form(request):
    
    return render (request, 'revisacion_medica/clientes_form.html')

def medicos_form(request):

    return render (request, 'revisacion_medica/medicos_form.html')

def revisacion_form(request):

    return render(request, 'revisacion_medica/revisacion_form.html')


