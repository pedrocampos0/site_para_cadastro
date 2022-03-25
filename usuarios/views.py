import csv

from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import UsuarioForm
from .models import Perfil


# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Lista_de_usuarios")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro inicial de novo usuário"
        context['botao'] = "Cadastrar"

        return context


class PerfilUpdate(UpdateView):
    template_name = "cadastros/dados_adicionais.html"
    model = Perfil
    fields = ["nome_completo", "data_de_nascimento"]
    success_url = reverse_lazy("inicio")

    def get_object(self, queryset=None):
        return get_object_or_404(Perfil, usuario=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Dados Adicionais Obrigatórios"
        context["botao"] = "Salvar"

        return context


class UsuariosList(ListView):
    model = Perfil
    template_name = 'perfil_list.html'


def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Nome Completo', 'Data de Nascimento'])

    for perfil in Perfil.objects.all().values_list('nome_completo', 'data_de_nascimento'):
        writer.writerow(perfil)

    response['Content-Disposition'] = 'attachment; filename="usuarioscadastrados.csv"'

    return response
