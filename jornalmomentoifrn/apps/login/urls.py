from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('cadastro/', CadastroView.as_view(), name='signup'),
]
