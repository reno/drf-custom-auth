# drf-custom-auth

![Django](https://img.shields.io/pypi/pyversions/Django) ![Django REST Framework](https://img.shields.io/pypi/djversions/djangorestframework) ![Travis](https://img.shields.io/travis/com/reno/drf-custom-auth) ![Coveralls](https://img.shields.io/coveralls/github/reno/drf-custom-auth)

Um app reutilizável de autenticação de usuário para Django REST Framework.

Este app tem como objetivo fornecer uma API de cadastro, autenticação e manutenção de usuários, utilizando recursos inclusos no Django e com um mínimo de dependências.

## ✨ Recursos

* Autenticação com JWT.
* Login com nome de usuário ou email.
* Endpoints para listagem, criação, detalhes, atualização e exclusão de usuários. Apenas usuários cadastrados podem listar usuários, e somente o próprio usuário pode ver detalhes, atualizar ou excluir seu cadastro.
* Confirmação de email no cadastro e reset de senha com envio de email.
* Modelo de usuário customizado, permitindo a inclusão de campos adicionais.

## 📌 Requisitos

- Python 3.6+

## ⚙️ Tecnologias utilizadas

- [Django REST Framework](https://www.django-rest-framework.org/) 
- [JWT](https://jwt.io/)
- [python-decouple](https://github.com/henriquebastos/python-decouple)

## 🚀 Uso

Primeiramente, crie um ambiente virtual:

`python -m venv venv`

Ative o ambiente virtual:

`source venv/bin/activate`

Instale o Django

`pip install django`

Inicialize um projeto usando este repositório como template:

`django-admin startproject --template=https://github.com/reno/drf-custom-auth/archive/master.zip <project_name> .`

Instale as dependências:

`pip install -r requirements.txt`

Execute as migrações do banco de dados:

`python manage.py migrate`

Finalmente, execute o servidor de desenvolvimento:

`python manage.py runserver`


## 🎯 Testes

Para executar os testes, após ativar o ambiente virtual e instalar as dependências, execute o comando:

`python manage.py test`
