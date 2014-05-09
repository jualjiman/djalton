from django.db import models

# Create your models here.
class Trabajo(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	imagen = models.FileField(upload_to = "portafolio")

	def __str__(self):
		return self.titulo
