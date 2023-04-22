from django.urls import path

from api.views import favorite_post, favorite_delete_post

urlpatterns = [
    path('photos/<int:pk>/favorite_post/', favorite_post, name='favorite_post'),
    path('photos/<int:pk>/favorite_delete_post/', favorite_delete_post, name='favorite_delete_post'),
]
