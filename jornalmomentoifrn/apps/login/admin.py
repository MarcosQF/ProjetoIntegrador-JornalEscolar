from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['email', 'nome_usuario', 'is_active', 'is_staff', 'date_joined', 'get_groups']
    list_filter = ['is_active', 'is_staff', 'date_joined']
    search_fields = ['email', 'nome_usuario']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'nome_usuario', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome_usuario', 'password1', 'password2'),
        }),
    )

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all().order_by('name')])

    get_groups.short_description = 'Grupos'


admin.site.register(CustomUser, CustomUserAdmin)
