from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, UsuariosList
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name='usuarios/form.html'
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registrar/", UsuarioCreate.as_view(), name='registrar'),
    path('atualizar_dados/', PerfilUpdate.as_view(), name='atualizar_dados'),
    path('listar/usuarios', UsuariosList.as_view(), name='cadastrados'),
    path('export/', views.export, name='exportar_dados')
]
