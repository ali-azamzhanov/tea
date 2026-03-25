from .base import BASE_DIR

STATIC_URL = 'back_static/'
STATIC_ROOT = BASE_DIR / 'back_static'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

MEDIA_URL = 'back_media/'
MEDIA_ROOT = BASE_DIR / 'back_media'

CKEDITOR_UPLOAD_PATH = 'ckeditor/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}
