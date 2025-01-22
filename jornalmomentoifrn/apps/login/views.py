from django.shortcuts import render
from django.views.generic import TemplateView

class LoginViews(TemplateView):
    template_name = "login/login.html"

class CadastroViews(TemplateView):
    template_name = "login/cadastro.html"
# Create your views here.
