from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import GroupCheckMixin

class IndexViews(GroupCheckMixin,TemplateView):
  template_name = "paginas/modelo.html"


class ModeloViews(TemplateView):
  template_name = "paginas/modelo.html"

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
  
