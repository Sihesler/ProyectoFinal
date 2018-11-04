from django.db import models
from django.contrib import admin


# Create your models here.
class Estudiante(models.Model):

    nombre           =  models.CharField(max_length=50)
    edad             =  models.IntegerField()
    fecha_nacimiento =  models.DateField()
    direccion        =  models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#////////////
class Curso(models.Model):

    nombre      = models.CharField(max_length=60)
    profesor    = models.CharField(max_length=60)
    hora        = models.CharField(max_length=20)
    estudiantes = models.ManyToManyField(Estudiante, through='Asignacion')

    def __str__(self):
        return self.nombre

#/////////
class Asignacion (models.Model):

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

#/////////
class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class EstudianteAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
