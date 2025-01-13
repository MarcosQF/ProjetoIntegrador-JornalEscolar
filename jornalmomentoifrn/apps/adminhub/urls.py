from django.urls import path
from .views import InitialDashboardViews,UsersDashboardViews

urlpatterns = [
    path('', InitialDashboardViews.as_view(), name="initial-dashboard-path"),
    path('usuarios/', UsersDashboardViews.as_view(), name="users-dashboard-path"),
]