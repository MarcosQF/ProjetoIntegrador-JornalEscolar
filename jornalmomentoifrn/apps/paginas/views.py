from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexViews(TemplateView):
  template_name = "paginas/index.html"

class ModeloViews(TemplateView):
  template_name = "paginas/modelo.html"

class MentesViews(TemplateView):
  template_name = "paginas/mentes.html"
