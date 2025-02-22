from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  
from .models import *

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
        required=False,
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
