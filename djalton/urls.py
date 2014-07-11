from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djalton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^herramientas/$', 'administrador.views.herramientas', name='herramientas'),
    url(r'^areas/$', 'administrador.views.areas', name='areas'),
    url(r'^ofertas/$', 'administrador.views.ofertas', name='ofertas'),
    url(r'^nosotros/$', 'administrador.views.nosotros', name='nosotros'),
    url(r'^portafolio/(\d+)/$', 'administrador.views.portafolioIndividual', name='portafolioIndividual'),
    url(r'^portafolio/$', 'administrador.views.portafolio', name='portafolio'),
    url(r'^contacto/$', 'administrador.views.contacto', name='contacto'),
    url(r'^contactoEmail/$', 'administrador.views.contactoEmail', name='contactoEmail'),
    url(r'^e404/$', 'administrador.views.e404', name='e404'),

)

urlpatterns += patterns('',url(r'^var/www/djporta/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)
urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),)
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)

handler404 = "administrador.views.e404"
