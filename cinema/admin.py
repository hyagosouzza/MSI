from django.contrib.admin import ModelAdmin, site
from .models import Cinema, Categoria, Filme, Sessao, Reserva


class CinemaAdmin(ModelAdmin):
    list_display = ['nome', 'endereco', 'cidade', 'estado', 'data_cadastro']
    search_fields = ['nome', 'cidade']


class CategoriaAdmin(ModelAdmin):
    list_display = ['nome', 'data_cadastro']
    search_fields = ['nome']


class FilmeAdmin(ModelAdmin):
    list_display = ['nome', 'categoria', 'classificacao']
    search_fields = ['nome', 'categoria__nome']


class SessaoAdmin(ModelAdmin):
    list_display = ['cinema', 'filme', 'tipo' ]
    search_fields = ['cinema__nome', 'filme__nome']


class ReservaAdmin(ModelAdmin):
    list_display = ['usuario', 'sessao', 'quantidade']
    search_fields = ['usuario__first_name', 'sessao__filme__nome']


site.register(Cinema, CinemaAdmin)
site.register(Categoria, CategoriaAdmin)
site.register(Filme, FilmeAdmin)
site.register(Sessao, SessaoAdmin)
site.register(Reserva, ReservaAdmin)
