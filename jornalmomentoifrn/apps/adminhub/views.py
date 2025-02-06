from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView,ListView,CreateView,UpdateView,DeleteView
from .forms import CreatePostForm,CategoriaForm,ImageUploadForm
from .models import *

class InitialDashboardViews(ListView):
  template_name = "adminhub/initial_dashboard.html"
  model = Categorias
  context_object_name = "categorias"

  def get_context_data(self, **kwargs):
        # Obtém o contexto padrão
      context = super().get_context_data(**kwargs)
        
        # Adiciona os dados dos dois modelos
      context['images'] = Banners.objects.all()
      context['categorias'] = Categorias.objects.all()
        
      return context

# Views Categoria
class CategoriaCreateView(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = "adminhub/categoria_form.html"
    success_url = reverse_lazy("initial-dashboard-path")

class CategoriaUpdateView(UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = "adminhub/categoria_form_update.html"
    success_url = reverse_lazy("initial-dashboard-path")
 
class CategoriaDeleteView(DeleteView):
    model = Categorias
    template_name = 'adminhub/categoria_confirm_delete.html'
    success_url = reverse_lazy('initial-dashboard-path')


class UsersDashboardViews(TemplateView):
  template_name = "adminhub/users.html"

class PostsDashboardViews(TemplateView):
  template_name = "adminhub/posts.html"

class ReportedCommentsViews(TemplateView):
  template_name = "adminhub/comment_reported.html"

class CreatePostViews(FormView):
    template_name = "adminhub/create_post.html"
    form_class = CreatePostForm  # O formulário que será exibido

    def form_valid(self, form):
        # Quando o formulário for válido, você pode processar os dados
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']

        # Aqui você pode processar o conteúdo, como salvar no banco de dados ou exibir uma mensagem
        print(f'Título: {title}, Conteúdo: {content}')  # Exemplo de como capturar os dados

        # Adicionando uma mensagem de sucesso ao contexto
        context = self.get_context_data(form=form)
        context['success_message'] = 'Post criado com sucesso!'  # Mensagem de sucesso
        return self.render_to_response(context)  # Renderizar a página com a mensagem de sucesso

    def form_invalid(self, form):
        # Se o formulário for inválido, você pode exibir erros na tela
        return super().form_invalid(form)
    
class BannerUploadView(CreateView):
    model = Banners
    form_class = ImageUploadForm
    template_name = 'adminhub/banner_upload.html'
    success_url = reverse_lazy('initial-dashboard-path')

class BannerUpdateView(UpdateView):
    model = Banners
    form_class = ImageUploadForm
    template_name = "adminhub/banner_update.html"
    success_url = reverse_lazy("initial-dashboard-path")
 
class BannerDeleteView(DeleteView):
    model = Banners
    template_name = 'adminhub/banner_delete.html'
    success_url = reverse_lazy('initial-dashboard-path')
