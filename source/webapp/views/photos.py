from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at',)


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm
    permission_denied_message = 'У вас нет прав доступа'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('index')


class PhotoUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'photo_update.html'
    model = Photo
    form_class = PhotoForm
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        return self.request.user.has_perm('webapp.change_photo') or (self.request.user.id == photo.author.id)

    def get_success_url(self):
        return reverse('index')


# , kwargs={'pk': self.object.pk}


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo




class PhotoDeleteView(UserPassesTestMixin, DeleteView):
    model = Photo
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        return self.request.user.has_perm('webapp.change_photo') or (self.request.user.id == photo.author.id)

    def get_success_url(self):
        return reverse('index')
