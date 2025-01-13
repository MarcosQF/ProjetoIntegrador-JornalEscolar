from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class InitialDashboardViews(TemplateView):
  template_name = "adminhub/initial_dashboard.html"


class UsersDashboardViews(TemplateView):
  template_name = "adminhub/users.html"