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

def areas(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"areas.html",{"ofertas":ofertas})

def ofertas(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"ofertas.html",{"ofertas":ofertas})

def nosotros(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"nosotros.html",{"ofertas":ofertas})

def portafolio(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"portafolio.html",{"ofertas":ofertas})

def contacto(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"contacto.html",{"ofertas":ofertas})



