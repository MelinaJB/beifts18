from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('hello/<str:username>', Hola.as_view(), name='hola'),
    path('proyecto', proyecto.as_view(), name='proyecto'),
    path('tareas', tareas.as_view(), name='tareas'),
    path('creartarea', crearTarea.as_view(), name='creartarea'),
    path('crearproyecto', crearProyecto.as_view(), name='crearproyecto'),
    path('detalleproyecto/<int:id>', detalleProyecto.as_view(), name='detalleproyecto'),
]