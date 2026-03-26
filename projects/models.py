from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnoligias = models.CharField(max_length=200)
    f_creacion = models.DateTimeField(auto_now_add=True)