from django.urls import path
from .views import IndexViews, ModeloViews, MentesViews, NoticiasViews, LogadoViews, PedidosViews, BaseViews

urlpatterns = [
    path('', IndexViews.as_view(), name="index"),
    path('base/', BaseViews.as_view(), name="base"),
    path('modelo/', ModeloViews.as_view(), name="modelo"),
    path('mentes/', MentesViews.as_view(), name="mentes"),
    path('noticias/', NoticiasViews.as_view(), name="noticias"),
    path('logado/', LogadoViews.as_view(), name="logado"),
    path('pedidos/', PedidosViews.as_view(), name="pedidos"),
]

