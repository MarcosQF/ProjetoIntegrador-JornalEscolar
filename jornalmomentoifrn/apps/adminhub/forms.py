from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Importação correta
from .models import Categorias


class CreatePostForm(forms.Form):
    title = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Escreva aqui o título '}),
        label='Título' 
    )

    CATEGORY_CHOICES = [
        ('', 'Categoria'),  # Opção default
        ('politica', 'Política'),
        ('economia', 'Economia'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('tecnologia', 'Tecnologia'),
        ('entretenimento', 'Entretenimento')
    ]
        
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        label='Categoria',
        widget=forms.Select(),
        required=True
    )

    content = forms.CharField(
        widget=CKEditorUploadingWidget(),  # Usando o widget correto para upload de arquivos
        label='Conteúdo' 
    )


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
