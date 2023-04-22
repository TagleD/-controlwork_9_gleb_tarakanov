from django.views.generic import TemplateView, ListView

from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('created_at',)

