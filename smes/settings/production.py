from .base import *

STATIC_ROOT = BASE_DIR.parent / 'static'
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR.parent / 'staticfiles'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = 'uploads/'
MEDIA_ROOT = BASE_DIR.parent / 'media'