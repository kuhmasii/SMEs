from .base import *


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent / 'static'
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [
    BASE_DIR.parent  / 'staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}

CSRF_TRUSTED_ORIGINS = ['https://smesbis.up.railway.app']
# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = 'uploads/'
MEDIA_ROOT = BASE_DIR.parent / 'media'