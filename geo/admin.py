from django.contrib.admin import ModelAdmin, site
from .models import Pais, Estado, Cidade


class PaisAdmin(ModelAdmin):
    list_display = ['nome','sigla','ativo']
    search_fields = ['nome']


class EstadoAdmin(ModelAdmin):
    list_display = ['nome','pais', 'ativo']
    search_fields = ['nome','pais__nome']


class CidadeAdmin(ModelAdmin):
    fields = ['nome','estado',]
    list_display = ['nome','estado','ativo',]
    search_fields = ['nome','estado__nome','estado__pais__nome']
    #list_editable = ['ordem']


site.register(Pais,PaisAdmin)
site.register(Estado,EstadoAdmin)
site.register(Cidade,CidadeAdmin)