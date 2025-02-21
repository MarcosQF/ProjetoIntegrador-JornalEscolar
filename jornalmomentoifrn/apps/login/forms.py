from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    nome_usuario = forms.CharField(max_length=100, label='Nome de Usuário')
    email = forms.EmailField(label='E-mail')
    imagem_perfil = forms.ImageField(required=False, label='Imagem de Perfil')

    class Meta:
        model = CustomUser
        fields = ('nome_usuario', 'email')

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('password1')  # 'password1' é o nome padrão do campo de senha no UserCreationForm
        confirmar_senha = self.cleaned_data.get('password2')  # 'password2' é o nome padrão do campo de confirmação

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return confirmar_senha
