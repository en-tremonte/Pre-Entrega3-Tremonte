from django.urls import path
from revisacion_medica import views

urlpatterns = [
    path('', views.inicio ),
    path('clientes', views.cliente),
    path('medicos', views.medico),
    path('revisaciones', views.revisaciones),
    
]

