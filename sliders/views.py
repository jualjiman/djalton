from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	sliders = Slider.objects.all()
	return render(request,"index.html",{"sliders": sliders})
