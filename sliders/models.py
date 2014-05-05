from django.db import models

# Create your models here.
class Slider(models.Model):
	title = models.CharField(max_length=160)
	image = models.FileField(upload_to = "sliders/assets")

	def __str__(self):
		return self.title

class Label(models.Model):
	title = models.CharField(max_length=50)
	slider = models.ForeignKey(Slider)

	def __str__(self):
		return self.title