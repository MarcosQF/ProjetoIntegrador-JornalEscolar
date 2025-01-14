from django.urls import path,include
from .views import InitialDashboardViews,UsersDashboardViews,CreatePostViews,PostsDashboardViews

urlpatterns = [
    path('', InitialDashboardViews.as_view(), name="initial-dashboard-path"),
    path('usuarios/', UsersDashboardViews.as_view(), name="users-dashboard-path"),
    path('noticias/criar_noticia/', CreatePostViews.as_view(), name="create-post-path"),
    path('noticias/', PostsDashboardViews.as_view(), name="posts-path"),
]