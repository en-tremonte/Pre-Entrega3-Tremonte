# Pre-Entrega3-Tremonte

En esta entrega se desarrollo un prototipo de web para registro y busqueda de revisaciones medicas para un natatorio. Esta pensada como para que el user sea personal del natatorio.

Al entrar a la web se ve una barra de navegacion que tiene un boton de inicio a la izquierda. 
La funcion del mismo es mostrar la vista de inicio. 
La vista de inicio consiste en la herencia de una vista padre.html la cual proviene de bootstrap. 

Hacia la derecha de la barra de navegacion se ven 3 botones. 1 por cada clase creada en models: 
    Clase clientes: En la web aparece como SOCIOS, por el simple hecho de que queda mejor. Al hacer click sobre el boton socios nos dirige a una vista heredada de padre.html (clientes.html). En esta vista vemos un boton que al apretarlo nos dirige un formulario que nos permite registrar un nuevo socio usando 3 atributos: Nombre, Apellido y Numero de socio. El formulario se encuentra en una vista heredada de padre.html y clientes.html (clientes_form.html)

    Clase Medicos: Al apretar sobre el boton de Medicos nos dirige a la vista medicos.html en donde encontramos 2 botones.Ambos nos dirigen a otras vistas heredadas que contienen formularios. Una vista lleva un formulario de registro de Medicos (medicos_form.html) en el cual se ingresan Nombre, Apellido y Numero de matricula. La otra vista (revisacion_form.html) nos lleva a un formulario de registro de la revisacion, el cual debe ser llenado por el medico, por eso se encuentran ambos botones en la vista medicos.html. En el registro de revisacion nos permite ingresar datos del socio (ya sea nombre y apellido o uno de los dos), datos del medico, fecha en el que se hizo la revisacion y el vencimiento. Se le agrega una casilla de check que indica que el socio es apto para entrar a la pileta. 

    Clase Revisaciones: contiene los atributos antes mencionados sobre la revisacion medica de cada socio. Sin embargo el ultimo boton no es de registro de revisaciones sino que nos lleva a una casilla de busqueda. Esta casilla sirve para ingresar datos de un socio para saber si ha realizado su revisacion y si está apto. De manera que nos devuelve los datos del socio, la fecha de la revisacion, la fecha de vencimiento y el valor True si está apto. 
    En caso de ingresar un dato erroneo a la busqueda nos devolvera un mensaje "no se ha encontrado la busqueda". 
    La casilla de busqueda pertenece a la plantilla revisacion.html, la cual es una plantilla heredada de padre.html. Los resultados de la busqueda pertenecen a la plantilla resultados_search.html

    En la vista de inicio, debajo de la barra de navegacion encontramos un mensaje del natatorio y en el footer datos genericos del natatorio ficticio. Todas las vistas heredadas se ubican entre el body y el footer. 

En el archivo views.py se encuentran las funciones que definen las vistas de cada clase, las funciones que definen los forms y la busqueda. 
En el archivo forms.py se encuentran las clases destinadas a los forms
en el archivo models.py se encuentran las clases elegidas para la entrega y a su vez una funcion __str__ para cada clase, de modo que el superuser pueda leer de manera ordeanada cada objeto. 
En el archivo admin.py se encuentran registradas las clases para para poder manipularlas como superuser.