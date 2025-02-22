class GroupCheckMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Verificar se o usuário pertence ao grupo 'Editor'
        context['is_editor'] = self.request.user.groups.filter(name='Editor').exists()
        return context