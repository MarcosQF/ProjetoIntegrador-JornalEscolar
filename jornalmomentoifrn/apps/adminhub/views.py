from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import CreatePostForm

class InitialDashboardViews(TemplateView):
  template_name = "adminhub/initial_dashboard.html"


class UsersDashboardViews(TemplateView):
  template_name = "adminhub/users.html"

class PostsDashboardViews(TemplateView):
  template_name = "adminhub/posts.html"

class CreatePostViews(FormView):
    template_name = "adminhub/create_post.html"
    form_class = CreatePostForm  # O formulário que será exibido

    def form_valid(self, form):
        # Quando o formulário for válido, você pode processar os dados
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']

        # Aqui você pode processar o conteúdo, como salvar no banco de dados ou exibir uma mensagem
        print(f'Título: {title}, Conteúdo: {content}')  # Exemplo de como capturar os dados

        # Adicionando uma mensagem de sucesso ao contexto
        context = self.get_context_data(form=form)
        context['success_message'] = 'Post criado com sucesso!'  # Mensagem de sucesso
        return self.render_to_response(context)  # Renderizar a página com a mensagem de sucesso

    def form_invalid(self, form):
        # Se o formulário for inválido, você pode exibir erros na tela
        return super().form_invalid(form)