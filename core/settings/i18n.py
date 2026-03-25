from .base import BASE_DIR

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_TZ = True

LANGUAGES = (
    ('ru', 'Русский'),
    ('ky', 'Кыргызский'),
    ('en', 'English'),
)

LOCALE_PATHS = [BASE_DIR / 'locale']
