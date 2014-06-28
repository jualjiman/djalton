from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from random import sample
from django.core.mail import send_mail
from .forms import ContactForm
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
	ofertas = Oferta.objects.all()[:5]
	trabajo = Trabajo.objects.get(pk=id)
	count = Trabajo.objects.all().count()
	rand_ids = sample(xrange(1, count), 2)
	trabajos = Trabajo.objects.filter(id__in=rand_ids)
	return render(request,"portafolio_single.html",{"trabajo":trabajo,"trabajos":trabajos})

# def contacto(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 		    name = form.cleaned_data['name']
# 		    email = form.cleaned_data['email']
# 		    phonenumber = form.cleaned_data['phonenumber']
# 		    message = form.cleaned_data['message']

# 		    subject = "Mensaje desde el sitio Daltonautomotriz.com"

# 		    fmessage = "Nombre: " + name + "\n" + "Numero telefonico: " + phonenumber + "\n" + "Email: " + email + "\n\n" + message

# 		    recipients = ['jualjiman@gmail.com']

# 		    send_mail(subject, fmessage, email, recipients)
# 		    return HttpResponseRedirect('/thanks/')
# 		else:
# 			ofertas = Oferta.objects.all()[:5]
# 			return render(request,"contacto.html",{"ofertas":ofertas,"form": form})
# 	else:
# 		ofertas = Oferta.objects.all()[:5]
# 		form = ContactForm()
# 		return render(request,"contacto.html",{"ofertas":ofertas,"form": form})

def contacto(request):
	ofertas = Oferta.objects.all()[:5]
	form = ContactForm()
	return render(request,"contacto.html",{"ofertas":ofertas,"form": form})

def contactoEmail(request):
	if request.is_ajax():
	    name = request.POST['name']
	    email = request.POST['email']
	    phonenumber = request.POST['phonenumber']
	    message = request.POST['message']

	    subject = "Mensaje desde el sitio Daltonautomotriz.com"

	    fmessage = "Nombre: " + name + "\n" + "Numero telefonico: " + phonenumber + "\n" + "Email: " + email + "\n\n" + message

	    recipients = ['jualjiman@gmail.com']

	    send_mail(subject, fmessage, email, recipients)
	    return HttpResponse('Ok')
	else:
		contacto(request)

def e404(request):
	ofertas = Oferta.objects.all()[:5]
	return render(request,"404.html",{"ofertas":ofertas})
