from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('created_at',)


class PhotoCreateView(CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('index')


class PhotoUpdateView(UpdateView):
    template_name = 'photo_update.html'
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('index')

# , kwargs={'pk': self.object.pk}


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo


class PhotoDeleteView(DeleteView):
    model = Photo

    def get_success_url(self):
        return reverse('index')
