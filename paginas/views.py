from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "usuario_logado.html"
class SobreView(TemplateView):
    template_name = "sobre.html"