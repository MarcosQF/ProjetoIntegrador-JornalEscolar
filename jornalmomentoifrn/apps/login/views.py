from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.paginas.mixins import GroupCheckMixin

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class CadastroView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'login/cadastro.html'
    success_url = reverse_lazy('login')

class CustomUserUpdateView(LoginRequiredMixin,GroupCheckMixin,UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'login/perfil.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user
