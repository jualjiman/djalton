from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'imagen_proyecto_slider')

	def imagen_proyecto_slider(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_proyecto_slider.allow_tags = True

class TrabajoAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion', 'imagen_proyecto_trabajo')

	def imagen_proyecto_trabajo(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_proyecto_trabajo.allow_tags = True

class OfertaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'descripcion','precio', 'imagen_proyecto_oferta')

	def imagen_proyecto_oferta(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_proyecto_oferta.allow_tags = True

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('nombre','cargo', 'imagen_proyecto_empleado')

	def imagen_proyecto_empleado(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_proyecto_empleado.allow_tags = True

admin.site.register(Slider,SliderAdmin)
admin.site.register(Trabajo,TrabajoAdmin)
admin.site.register(Oferta,OfertaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
