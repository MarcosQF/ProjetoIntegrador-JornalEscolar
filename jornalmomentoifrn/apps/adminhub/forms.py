from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Importação correta

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

