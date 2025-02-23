from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

class Noticias(models.Model):
    title = models.CharField(max_length=80)
    content = RichTextUploadingField(blank=False)  
    category = models.ForeignKey('Categorias', on_delete=models.CASCADE)
    thumb = models.ImageField(upload_to='noticias/thumbs/',blank=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='noticias')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Categorias(models.Model):
    nome_categoria = models.CharField(max_length=20,unique=True,blank=False) 

    def __str__(self):
        return self.nome_categoria

class Banners(models.Model):
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return f"Image {self.id}"
