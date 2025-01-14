from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class Artigo(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()  # Usando o campo do CKEditor para conteúdo com imagens

    def __str__(self):
        return self.titulo