from django.db import models

# Create your models here.

class Proyecto(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
  

class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo + ' - ' + self.descripcion