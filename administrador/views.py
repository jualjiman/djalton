from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	sliders = Slider.objects.all()
	ofertas = Slider.objects.all()[3:]
	return render(request,"index.html",{"sliders": sliders,"ofertas":ofertas})