from django.urls import path
from .views import *


urlpatterns = [
        path("", index, name= 'index'),
        path("autor/", list_autor_view, name='list_autor'),
        path("autor/create", novo_autor_view, name='novo_autor'),
        path("autor/edit/<int:id>", editar_autor_view, name='editar_autor'),
        path("autor/delete/<int:id>", delete_autor_view, name='delete_autor'),

        path("auxiliar/", list_auxiliar_view, name='list_auxiliar'),
        path("auxiliar/create", novo_auxiliar_view, name='novo_auxiliar'),
        path("auxiliar/edit/<int:id>", editar_auxiliar_view, name='editar_auxiliar'),
        path("auxiliar/delete/<int:id>", delete_auxiliar_view, name='delete_auxilia'),

        #avaliador
        path("avaliador/", listar_avaliador_view, name='list_avaliador'),
        path("avaliador/create", novo_avaliador_view, name='novo_avaliador'),
        path("avaliador/edit/<int:id>", editar_avaliador_view, name='editar_avaliador'),
        path("avaliador/delete/<int:id>", delete_avaliador_view, name='delete_avaliador'),


        path("projeto/", ProjetoListView.as_view(), name='list_projeto'),
        path('projetos-nao-avaliados/', projetos_nao_avaliados, name='projetos_nao_avaliados'),
        path("projeto/<int:pk>", DetalheProjeto.as_view(), name='detalhe_projeto'),
        path('projeto/<int:pk>/adicionar-nota/', DetalheProjeto.as_view(), name='adicionar_nota'),
        path("projeto/create", novo_projeto_view, name='novo_projeto'),
        path("projeto/edit/<int:id>", editar_projeto_view, name='editar_projeto'),
        path("projeto/delete/<int:id>", delete_projeto_view, name='delete_projeto'),

        #
        path("premio/", listar_premio_view, name='lista_premio'),
        path("premio/create", inserir_premio_view, name='inserir_premio_view'),
        path("premio/edit/<int:id>", editar_premio_view, name='editar_premio'),
        path("premio/delete/<int:id>", delete_premio_view, name='delete_premio'),



]