"""
WSGI config for djalton project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djalton.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

"""

import os, sys
sys.path.append('/webapps/djaltonc/djalton')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djalton.settings'

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
	environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
	
	if environ['wsgi.url_scheme'] == 'https':
		environ['HTTPS'] = 'on'
	
	return _application(environ, start_response)
