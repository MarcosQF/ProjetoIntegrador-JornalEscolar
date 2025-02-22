from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, CategoriaForm, ImageUploadForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class InitialDashboardViews(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "adminhub/initial_dashboard.html"
    model = Categorias

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['images'] = Banners.objects.all()
        context['categorias'] = Categorias.objects.all()

        return context


# Views Categoria
class CategoriaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = "adminhub/categoria_form.html"
    success_url = reverse_lazy("initial-dashboard-path")

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class CategoriaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = "adminhub/categoria_form_update.html"
    success_url = reverse_lazy("initial-dashboard-path")

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class CategoriaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Categorias
    template_name = 'adminhub/categoria_confirm_delete.html'
    success_url = reverse_lazy('initial-dashboard-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class UsersDashboardViews(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "adminhub/users.html"

    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()

class ReportedCommentsViews(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "adminhub/comment_reported.html"

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

# Vies Noticias
class CreateNoticiaView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Noticias
    template_name = "adminhub/create_post.html"
    form_class = CreatePostForm
    success_url = reverse_lazy("posts-path")

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class ListNoticiaViews(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "adminhub/posts.html"
    model = Noticias
    context_object_name = "noticias"

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class DeleteNoticiaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Noticias
    template_name = "adminhub/noticia_delete.html"
    success_url = reverse_lazy('posts-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class BannerUploadView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Banners
    form_class = ImageUploadForm
    template_name = 'adminhub/banner_upload.html'
    success_url = reverse_lazy('initial-dashboard-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class BannerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Banners
    form_class = ImageUploadForm
    template_name = "adminhub/banner_update.html"
    success_url = reverse_lazy("initial-dashboard-path")

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class BannerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Banners
    template_name = 'adminhub/banner_delete.html'
    success_url = reverse_lazy('initial-dashboard-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()