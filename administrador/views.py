from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	sliders = Slider.objects.all()
	ofertas = Oferta.objects.all()[:5]
	trabajos = Trabajo.objects.all()[:3]
	return render(request,"index.html",{"sliders": sliders,"ofertas":ofertas,"trabajos":trabajos})

def herramientas(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"herramientas.html",{"ofertas":ofertas})
