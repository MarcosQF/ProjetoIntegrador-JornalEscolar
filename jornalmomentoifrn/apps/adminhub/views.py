
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .forms import CreatePostForm,CategoriaForm,ImageUploadForm
from .models import *

class InitialDashboardViews(ListView):
  template_name = "adminhub/initial_dashboard.html"
  model = Categorias
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
        
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

class ReportedCommentsViews(TemplateView):
  template_name = "adminhub/comment_reported.html"

#Vies Noticias
class CreateNoticiaView(CreateView):
  model = Noticias  
  template_name = "adminhub/create_post.html"  
  form_class = CreatePostForm  
  success_url = reverse_lazy("posts-path")

class ListNoticiaViews(ListView):
  template_name = "adminhub/posts.html"
  model = Noticias
  context_object_name = "noticias"

class DeleteNoticiaView(DeleteView):
  model = Noticias
  template_name = "adminhub/noticia_delete.html"
  success_url = reverse_lazy('posts-path')
    
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
