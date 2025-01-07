from django.urls import path
from .views import IndexViews, ModeloViews

urlpatterns = [
    path('inicio/', IndexViews.as_view(), name="index"),
    path('modelo/', ModeloViews.as_view(), name="modelo"),
]
