from django.contrib import admin
from .models import Autor,Auxiliar, Avaliador, Premio, EnviarProjeto, ProjetoAvaliado


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome')


@admin.register(Auxiliar)
class AuxiliarAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome')


@admin.register(EnviarProjeto)
class EnviarProjetoAdmin(admin.ModelAdmin):
    list_filter = ('id', 'area','titulo','dataEnvio')


@admin.register(Avaliador)
class AvaliadorAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome')


@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome', 'descricao')


@admin.register(ProjetoAvaliado)
class ProjetoAvaliadoAdmin(admin.ModelAdmin):
    list_filter = ('id' , 'avaliador', 'projeto')
