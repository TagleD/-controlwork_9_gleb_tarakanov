from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from webapp.models import Photo


def favorite_post(request, *args, **kwargs):
    photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
    photo.user_favorites.add(request.user)
    return JsonResponse({'status': 'ok'}, status=200)


def favorite_delete_post(request, *args, **kwargs):
    photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
    photo.user_favorites.remove(request.user)
    return JsonResponse({'status': 'ok'})
