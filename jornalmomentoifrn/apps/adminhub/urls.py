from django.urls import path
from .views import InitialDashboardViews

urlpatterns = [
    path('', InitialDashboardViews.as_view(), name="initial-dashboard-path"),
]