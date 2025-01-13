from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def mentes(request):
  return render(request, 'paginas/mentes.html')

class IndexViews(TemplateView):
  template_name = "paginas/index.html"

class ModeloViews(TemplateView):
  template_name = "paginas/modelo.html"

