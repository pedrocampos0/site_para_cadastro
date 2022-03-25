# Passo a passo de utilização da API.
- No terminal utilize os comandos:

*cd site_para_cadastro*

*pip install django (caso não instalado)*

*pip install django-crispy-forms (caso não instalado)*

*py manage.py runserver*

- Após isso vá para a [Página inicial](http://127.0.0.1:8000).
- Depois realize o [Cadastro](http://127.0.0.1:8000/registrar) de usuário.
- Agora com o cadastro finalizado, você será automaticamente redirecionado para a página de Login, utilize o usuário e senha cadastrados.
- Logado, o usuário deverá terminar o cadastro de perfil, para isso colocando o nome completo e a data de nascimento.
- Após finalizada as etapas acima, o usuário finalmente poderá ver a lista de usuários cadastrados em [HTML](http://127.0.0.1:8000/listar/usuarios) ou exportar em [.csv](http://127.0.0.1:8000/export/).
