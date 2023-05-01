# Pre-Entrega3-Tremonte



En esta entrega se propone la idea de una posible web que pertenece a un club natatorio y tiene como funcion el registro y busqueda de revisaciones medicas para permitir el paso a la pileta. 

La idea de esta web es que el user sea el personal del natatorio, por lo que las acciones permitidas son: Registro de Clientes/socios - Registro de medicos - Registro de revisaciones medicas. Asi tambien esta web tiene una opcion para buscar revisaciones realizadas y ver su estado para permitir el ingreso de socios a la pileta. 

De esta manera se crearon 3 clases como models: 
    
    La clase clientes (quienes en la web aparecen como socios): estos tienen 3 atributos por cada cliente. Un nombre, un apellido y un numero de socio. 
    
    La clase Medicos: estos tienen tambien 3 atributos por medico. Un nombre, un apellido y un numero de matricula habilitante. 
    
    La clase Revisaciones : en este caso hay 5 atributos. Datos del socio revisado, Datos del medico que efectuó la revisacion, fecha de la revisacion y fecha en la que vence la misma y por ultimo el apto (significa si el socio esta apto o no para entrar a la pileta). 

En la web se podrá ver en la barra de navegacion un boton de inicio, uno que dice socios, uno que dice medicos y uno que dice revisaciones. 
El boton de inicio 

