from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CreatePostForm, CategoriaForm, ImageUploadForm, UserGroupForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ..login.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib import messages

class InitialDashboardViews(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "adminhub/initial_dashboard.html"
    model = Categorias

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['images'] = Banners.objects.all()
        context['categorias'] = Categorias.objects.all()
        context['users_total'] = CustomUser.objects.count()
        context['noticias_total'] = Noticias.objects.count()

        return context


# Views Categoria
class CategoriaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = "adminhub/categoria_form.html"
    success_url = reverse_lazy("initial-dashboard-path")

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Categoria criada com sucesso!')

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class CategoriaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = "adminhub/categoria_form_update.html"
    success_url = reverse_lazy("initial-dashboard-path")

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Categoria Alterada com sucesso!')

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class CategoriaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Categorias
    template_name = 'adminhub/categoria_confirm_delete.html'
    success_url = reverse_lazy('initial-dashboard-path')

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Categoria Deletada!')

        return response

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class UsersDashboardViews(LoginRequiredMixin, UserPassesTestMixin,ListView):
    template_name = "adminhub/users.html"
    model = CustomUser
    context_object_name = "usuarios"

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

    def form_valid(self, form):
        form.instance.autor = self.request.user

        response = super().form_valid(form)
        messages.success(self.request, 'Noticia criada com sucesso!')
        return super().form_valid(form)

class UpdateNoticiaView(LoginRequiredMixin,  UpdateView):
    model = Noticias
    template_name = "adminhub/update_post.html"
    form_class = CreatePostForm
    success_url = reverse_lazy("posts-path")

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Noticia Alterada com sucesso!')
        return super().form_valid(form)

class ListNoticiaViews(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "adminhub/posts.html"
    model = Noticias
    context_object_name = "noticias"

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

class NoticiaDetailView(DetailView):
    model = Noticias
    template_name = "paginas/noticias.html"
    context_object_name = "noticia"

class NoticiasListView(ListView):
    model = Noticias
    template_name = 'paginas/lista_noticias.html'
    context_object_name = 'noticias'
    paginate_by = 4
    ordering = ['-data_criacao']

    def get_queryset(self):
        queryset = super().get_queryset()

        titulo = self.request.GET.get('titulo', '')
        if titulo:
            queryset = queryset.filter(title__icontains=titulo)

        categoria = self.request.GET.get('categoria', '')
        if categoria:
            queryset = queryset.filter(category__nome_categoria=categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categorias'] = Categorias.objects.all()
        return context


class DeleteNoticiaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Noticias
    template_name = "adminhub/noticia_delete.html"
    success_url = reverse_lazy('posts-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Noticia Deletada com sucesso!')

        return response

class BannerUploadView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Banners
    form_class = ImageUploadForm
    template_name = 'adminhub/banner_upload.html'
    success_url = reverse_lazy('initial-dashboard-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Banner Criado com sucesso!')

        return response


#Banner Views
class BannerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Banners
    form_class = ImageUploadForm
    template_name = "adminhub/banner_update.html"
    success_url = reverse_lazy("initial-dashboard-path")

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Banner alterado com sucesso!')

        return response


class BannerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Banners
    template_name = 'adminhub/banner_delete.html'
    success_url = reverse_lazy('initial-dashboard-path')

    def test_func(self):
        return self.request.user.groups.filter(name='Editor').exists()

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Banner deletado com sucesso!')

        return response


class AddGroupToUser(LoginRequiredMixin,UpdateView):
    model = CustomUser
    form_class = UserGroupForm
    template_name = 'adminhub/user_form_add.html'
    success_url = reverse_lazy('users-dashboard-path')

    def form_valid(self, form):
        grupo = form.cleaned_data['group']
        usuario = self.get_object()
        usuario.groups.add(grupo)
        usuario.save()

        response = super().form_valid(form)
        messages.success(self.request, 'Grupo Editor adicionado com sucesso!')

        return super().form_valid(form)

class RemoveGroupFromUser(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserGroupForm
    template_name = 'adminhub/user_form_remove.html'
    success_url = reverse_lazy('users-dashboard-path')

    def form_valid(self, form):
        grupo = form.cleaned_data['group']
        usuario = self.get_object()
        usuario.groups.remove(grupo)
        usuario.save()

        response = super().form_valid(form)
        messages.success(self.request, 'Grupo Editor removido com sucesso!')
        return super().form_valid(form)





