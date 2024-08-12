# To-do App

## Descripción

To-Do App es una aplicación simple para la gestión de tareas. Permite a los usuarios crear, completar y eliminar tareas de manera fácil y organizada. La aplicación cuenta con una interfaz gráfica amigable desarrollada con PySide6 y está diseñada para ser fácil de usar.

## Funcionalidades

- Agregar Tareas: Los usuarios pueden agregar nuevas tareas especificando un título, descripción y fecha de vencimiento.
- Completar Tareas: Las tareas pueden marcarse como completadas, lo que cambia su estilo visual y las desactiva.
- Eliminar Tareas: Las tareas pueden eliminarse de la lista.
Contador de Tareas: La aplicación cuenta con un contador de tareas completadas e incompletas.

## Estructura del Proyecto

- main.py: Contiene la clase Mainwindow, que es la ventana principal de la aplicación donde se muestran y gestionan las tareas.
- addtask.py: Contiene la clase Addtask, que es la ventana donde se crean nuevas tareas.
- list_item_widget.py: Contiene la clase ListItemWidget, que define el formato visual de cada tarea en la lista.
- routes.py: Contiene la clase RouteManager, que se encarga de manejar la navegación entre las diferentes ventanas de la aplicación.

## Requisitos

- Python 3.8+
- PySide6

## Uso

Al iniciar la aplicación, verás la ventana principal con una lista de tareas.
Para agregar una tarea, presiona el botón "Agregar". Se abrirá una nueva ventana donde podrás ingresar el título, la descripción y la fecha de vencimiento de la tarea.
Para completar una tarea, selecciónala en la lista y presiona el botón "Completar".
Para eliminar una tarea, selecciónala en la lista y presiona el botón "Eliminar".
