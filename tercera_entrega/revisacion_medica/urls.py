from django.urls import path
from revisacion_medica import views

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('/socios', views.cliente, name = 'Socios'),
    path('/medicos', views.medico, name = 'Medicos'),
    path('/revisaciones', views.revisaciones, name = 'Revisaciones'),
    path('/clientes_form/', views.clientes_form, name='clientes_form'),
    path('/medicos_form/', views.medicos_form, name ='medicos_form'),
    path('/revisacion_form/', views.revisacion_form, name = 'revisacion_form'),
    path('/busqueda_revisacion/', views.busqueda_revisacion, name='busqueda_revisacion'),
    path('/buscar/', views.buscar, name='buscar'),
    

    
]

