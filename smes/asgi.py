"""
ASGI config for smes project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from decouple import config
from django.core.asgi import get_asgi_application


mode = config('MODE')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'smes.settings.{mode}')

application = get_asgi_application()
