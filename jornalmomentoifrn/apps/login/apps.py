from django.apps import AppConfig

class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.login'

class AccountsConfig(AppConfig):
    name = 'login'

    def ready(self):
        import login.signals.py