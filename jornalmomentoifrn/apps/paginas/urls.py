from django.urls import path
from .views import IndexViews, ModeloViews,MentesViews

urlpatterns = [
    path('', IndexViews.as_view(), name="index"),
    path('modelo/', ModeloViews.as_view(), name="modelo"),
    path('mentes/', MentesViews.as_view(), name="mentes"),
]

