# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Slider(models.Model):
	titulo = models.CharField(max_length=60)
	imagen = ImageField(upload_to = "sliders")
	etiqueta1 = models.CharField(max_length=25, blank=True)
	etiqueta2 = models.CharField(max_length=25, blank=True)
	etiqueta3 = models.CharField(max_length=25, blank=True)
	precio = models.CharField(max_length=15,blank=True)

	def __str__(self):
		return self.titulo

class Oferta(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	imagen = ImageField(upload_to = "ofertas")
	etiqueta1 = models.CharField(max_length=25, blank=True)
	etiqueta2 = models.CharField(max_length=25, blank=True)
	etiqueta3 = models.CharField(max_length=25, blank=True)
	precio = models.CharField(max_length=15,blank=True)

	def __str__(self):
		return self.titulo

class Trabajo(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	imagenPortada = ImageField(upload_to = "portafolio")
	imagen1 = ImageField(upload_to = "portafolio", blank=True)
	imagen2 = ImageField(upload_to = "portafolio",blank=True)
	imagen3 = ImageField(upload_to = "portafolio",blank=True)



	def __str__(self):
		return self.titulo
