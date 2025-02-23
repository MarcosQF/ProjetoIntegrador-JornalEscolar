from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView
from .mixins import GroupCheckMixin
from apps.adminhub.models import Noticias, Banners

class IndexViews(GroupCheckMixin,ListView):
    template_name = "paginas/modelo.html"
    model = Noticias

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['banners'] = Banners.objects.all()
        context['noticias'] = Noticias.objects.all()[:3]

        return context


class MentesViews(TemplateView):
  template_name = "paginas/mentes.html"

class NoticiasViews(TemplateView):
  template_name = "paginas/noticias.html"

class LogadoViews(TemplateView):
  template_name = "paginas/logado.html"
  
class PedidosViews(TemplateView):
  template_name = "paginas/pedidos.html"
  
class BaseViews(TemplateView):
  template_name = "paginas/base_paginas.html"
  
