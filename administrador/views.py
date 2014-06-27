from django.shortcuts import render
from .models import *
from random import sample
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
	ofertas = Oferta.objects.all()
	return render(request,"ofertas.html",{"ofertas":ofertas})

def nosotros(request):
	ofertas = Oferta.objects.all()[:5]
	empleados = Empleado.objects.all()
	return render(request,"nosotros.html",{"ofertas":ofertas,"empleados":empleados})

def portafolio(request):
	ofertas = Oferta.objects.all()[:5]
	trabajos = Trabajo.objects.all()
	return render(request,"portafolio.html",{"ofertas":ofertas,"trabajos":trabajos})

def portafolioIndividual(request,id):
	trabajo = Trabajo.objects.get(pk=id)
	count = Trabajo.objecs.all().count()
	rand_ids = sample(xrange(1, count), 2)
	trabajos = Trabajo.objects.filter(id__in=rand_ids)
	return render(request,"portafolio_single.html",{"trabajo":trabajo,"trabajos":trabajos})

def contacto(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"contacto.html",{"ofertas":ofertas})



