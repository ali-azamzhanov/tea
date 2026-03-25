from decouple import config
from importlib import import_module


def _load(module_name: str) -> None:
    module = import_module(f'core.settings.{module_name}')
    for k, v in module.__dict__.items():
        if k.isupper():
            globals()[k] = v


for _m in (
    'base',
    'auth',
    'i18n',
    'static_files',
    'api',
    'cors',
    'email',
    'security',
):
    _load(_m)

PRODUCTION = config('PRODUCTION', default=False, cast=bool)
_load('production' if PRODUCTION else 'development')
