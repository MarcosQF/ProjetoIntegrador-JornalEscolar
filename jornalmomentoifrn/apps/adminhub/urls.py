from django.urls import path
from .views import *

urlpatterns = [
    path('', InitialDashboardViews.as_view(), name="initial-dashboard-path"),
    path('usuarios/', UsersDashboardViews.as_view(), name="users-dashboard-path"),
    path('noticias/criar_noticia/', CreatePostViews.as_view(), name="create-post-path"),
    path('noticias/', PostsDashboardViews.as_view(), name="posts-path"),
    path('comentarios_denunciados/', ReportedCommentsViews.as_view(), name="comments-path"),
    path('categorias/criar', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/editar/<int:pk>', CategoriaUpdateView.as_view(), name='categoria-edit'),
    path('categorias/deletar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('banners/criar', BannerUploadView.as_view(), name='banner-create'),
    path('banners/editar/<int:pk>', BannerUpdateView.as_view(), name='banner-edit'),
    path('banners/deletar/<int:pk>/', BannerDeleteView.as_view(), name='banner-delete'),
    
]