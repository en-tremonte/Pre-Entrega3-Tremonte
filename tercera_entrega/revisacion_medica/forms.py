from django import forms

class Clientes_form(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numero_socio = forms.IntegerField()

class Medicos_form(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    matricula = forms.IntegerField()

class Revisaciones_form(forms.Form):
    datos_socio = forms.CharField()
    datos_medico =forms.CharField()
    fecha_revisacion = forms.DateField()
    fecha_vencimiento = forms.DateField()
    apto = forms.BooleanField()


