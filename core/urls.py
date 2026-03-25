from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(
            url_name='schema' if settings.DEBUG else None,
            url=None if settings.DEBUG else '/back_static/schema.yml',
        ),
        name='swagger-ui',
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(
            url_name='schema' if settings.DEBUG else None,
            url=None if settings.DEBUG else '/back_static/schema.yml',
        ),
        name='redoc',
    ),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/home-street/', include('apps.home_street.urls')),
]

if settings.DEBUG:
    urlpatterns.insert(1, path('schema/', SpectacularAPIView.as_view(), name='schema'))

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
else:
    urlpatterns += [
        re_path(r'^back_media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^back_static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
