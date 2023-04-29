from django.db import models

# Los modelos aquí creados pertenecen a la lógica de un club con pileta que realiza revisaciones médicas para el ingreso a la misma. 


class clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_socio= models.IntegerField()

class medicos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula = models.IntegerField()    

class revisacion(models.Model):
    nombre_cliente = clientes.nombre
    apellido_cliente = clientes.apellido

    fecha_revisacion = models.DateField()
    fecha_vencimiento = models.DateField()
    apto = models.BooleanField() 

    medico = medicos.matricula