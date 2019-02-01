"""
WSGI config for paas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import sys

sys.path.append('/var/www/html/mprdev')
sys.path.append('/var/www/html/mprdev/myenv/lib/python3.6/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apis.settings.dev")

application = get_wsgi_application()
