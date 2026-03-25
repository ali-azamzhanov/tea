from django.urls import path
from django.http import JsonResponse


def profile_view(request):
    return JsonResponse({'detail': 'Users app is working'})

urlpatterns = [
    path('profile/', profile_view, name='users-profile'),
]
