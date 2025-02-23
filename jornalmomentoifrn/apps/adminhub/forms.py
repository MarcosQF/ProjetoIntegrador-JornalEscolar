from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  
from .models import *
from ..login.models import CustomUser
from django.contrib.auth.models import Group


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Escreva aqui o título'}),
        label="Título",
    )

    content = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label="Conteúdo",
    )

    thumb = forms.ImageField(
        required=True,
        label="Imagem de Capa"
    )

    category = forms.ModelChoiceField(queryset=Categorias.objects.all(), empty_label="Selecione uma categoria")
    
    class Meta:
        model = Noticias
        fields = ['title', 'content', 'category', 'thumb']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nome_categoria']
        widgets = {
            'nome_categoria': forms.TextInput(attrs={
                'class': ' border-2 rounded-0',  
                'placeholder': 'Digite o nome da categoria'  
            }),
        }

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Banners
        fields = ['image']

class UserGroupForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.filter(name='Editor'),
        required=True,
        label="Grupo"
    )

    class Meta:
        model = CustomUser
        fields = ['group']

    def save(self, commit=True):
        user = super().save(commit=False)

        if user.groups.filter(name='Editor').exists():
            user.is_staff = True
        else:
            user.is_staff = False

        if commit:
            user.save()

        return user




