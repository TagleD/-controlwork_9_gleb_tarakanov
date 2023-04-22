from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from accounts.forms import CustomUserCreationForm, LoginForm, UserForm


# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('index')
        next = request.GET.get('next')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')


class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


def logout_view(request):
    logout(request)
    return redirect('index')


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = get_user_model()
    context_object_name = 'user_obj'


class UserUpdateView(UpdateView):
    template_name = 'user_update.html'
    model = get_user_model()
    form_class = UserForm

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})
