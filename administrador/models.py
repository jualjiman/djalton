# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Slider(models.Model):
	titulo = models.CharField(max_length=60)
	etiqueta1 = models.CharField(max_length=40, blank=True)
	etiqueta2 = models.CharField(max_length=40, blank=True)
	etiqueta3 = models.CharField(max_length=40, blank=True)
	precio = models.CharField(max_length=15,blank=True)
	imagen = ImageField(upload_to = "sliders")
	activo = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo

class Oferta(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	etiqueta1 = models.CharField(max_length=25, blank=True)
	etiqueta2 = models.CharField(max_length=25, blank=True)
	etiqueta3 = models.CharField(max_length=25, blank=True)
	precio = models.CharField(max_length=15,blank=True)
	imagen = ImageField(upload_to = "ofertas")
	activa = models.BooleanField(default=False)


	def __str__(self):
		return self.titulo

class Trabajo(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	imagenPortada = ImageField(upload_to = "portafolio")
	imagen1 = ImageField(upload_to = "portafolio", blank=True)
	imagen2 = ImageField(upload_to = "portafolio",blank=True)
	imagen3 = ImageField(upload_to = "portafolio",blank=True)
	activo = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo

class Empleado(models.Model):
	nombre = models.CharField(max_length=60)
	cargo = models.CharField(max_length=60)
	imagen = ImageField(upload_to = "empleado")
	activo = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre
