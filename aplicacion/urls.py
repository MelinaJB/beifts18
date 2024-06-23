from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('hello/<str:username>', Hola.as_view()),
    path('proyecto', proyecto.as_view()),
    path('tareas', tareas.as_view()),
    path('creartarea', crearTarea.as_view()),
    path('crearproyecto', crearProyecto.as_view()),
]