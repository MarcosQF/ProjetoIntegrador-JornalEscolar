from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    nome_usuario = forms.CharField(max_length=100, label='Nome de Usuário')
    email = forms.EmailField(label='E-mail')
    imagem_perfil = forms.ImageField(required=False, label='Imagem de Perfil')

    class Meta:
        model = CustomUser
        fields = ('nome_usuario', 'email', 'imagem_perfil')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.nome_usuario = self.cleaned_data['nome_usuario']
        if commit:
            user.set_password(self.cleaned_data['password1'])  # Usando password1
            user.save()
            
        group = Group.objects.get(name='Leitor')
        user.groups.add(group)

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'imagem_perfil', 'nome_usuario']
