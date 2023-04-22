from django.urls import path

from webapp.views.photos import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]