from django.urls import path
from revisacion_medica import views

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('socios', views.cliente, name = 'Socios'),
    path('medicos', views.medico, name = 'Medicos'),
    path('revisaciones', views.revisaciones, name = 'Revisaciones'),
    path('formulario socios', views.clientes_form, name='Registro Socios'),
    path('formulario medicos', views.medicos_form, name ='Registro Médicos'),
    path('formulario revisacion', views.revisacion_form, name = 'Registro Revisacion')
    
]

