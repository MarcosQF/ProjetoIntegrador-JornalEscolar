from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome_usuario, password=None, **extra_fields):
        if not email:
            raise ValueError(_('O e-mail deve ser informado'))
        email = self.normalize_email(email)
        user = self.model(email=email, nome_usuario=nome_usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome_usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nome_usuario, password, **extra_fields)



class CustomUser(AbstractUser):
    username = None
    nome_usuario = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    imagem_perfil = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_usuario']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
