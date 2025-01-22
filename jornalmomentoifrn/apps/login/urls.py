from django.urls import path
from .views import LoginViews, CadastroViews

urlpatterns = [
    path('', LoginViews.as_view(), name='login'),
    path('signup/', CadastroViews.as_view(), name='signup'),
]
