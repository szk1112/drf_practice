"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

app_env = os.environ.get("APP_ENV", "local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings." + app_env)

application = get_wsgi_application()
