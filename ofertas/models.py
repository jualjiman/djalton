from django.db import models

# Create your models here.
class Oferta(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	imagen = models.FileField(upload_to = "ofertas")
	etiqueta1 = models.CharField(max_length=25, blank=True)
	etiqueta2 = models.CharField(max_length=25, blank=True)
	etiqueta3 = models.CharField(max_length=25, blank=True)
	precio = models.CharField(max_length=15,blank=True)

	def __str__(self):
		return self.titulo