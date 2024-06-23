from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .forms import *

from .models import *

# Create your views here.


class Index(View):
    def get(self, request):
        title = 'Curso de Django :D'
        return render(request, 'index.html', {
            'title': title
        })


class Hola(View):
    def get(self, request, username):
        return HttpResponse("Hola %s" % username)


class proyecto(View):
    def get(self, request):
        # proyecto = list(Proyecto.objects.values())
        proyecto = Proyecto.objects.all()
        return render(request, 'proyecto.html', {
            'proyecto': proyecto
        })


class tareas(View):
    def get(self, request):  # elimine el parametro id
        # tareas = get_object_or_404(Tareas, id=id)
        tareas = Tareas.objects.all()
        return render(request, 'tareas.html', {
            'tareas': tareas
        })


class crearTarea(View):
    def get(self, request):
        # print(request.GET['titulo'])
        # print(request.GET['descripcion'])
        return render(request, 'crear_tarea.html', {
            'form': createNewTask()
        })

    def post(self, request):
        form = createNewTask(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            proyecto_id = 2
            Tareas.objects.create(
                titulo=titulo, descripcion=descripcion, proyecto_id=proyecto_id)
            return redirect('tareas')
        return render(request, 'crear_tarea.html', {
            'form': form
        })


class crearProyecto(View):
    def get(self, request):
        return render(request, 'crear_proyecto.html', {
            'form': createNewProject()
        })
    
    def post(self, request):
        form = createNewProject(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Proyecto.objects.create(name=name)
            return redirect('proyecto')
        return render(request, 'crear_proyecto.html', {
            'form': form
        })

class detalleProyecto(View):
    def get(self, request, id):
        #proyecto = Proyecto.objects.get(id=id)
        proyecto = get_object_or_404(Proyecto, id=id)
        tareas = Tareas.objects.filter(proyecto_id=id)
        return render(request, 'detalleproyecto.html', {
            'proyecto': proyecto,
            'tareas': tareas
        })