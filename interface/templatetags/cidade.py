from django import template
from django.utils.safestring import mark_safe

from cinema.models import Cinema
from geo.models import Cidade

register = template.Library()


@register.filter
def cidade_atual(request):
    cidade = request.session.get("cidade")
    if not cidade or not isinstance(cidade, int):
        if request.user.is_authenticated:
            cidade = request.user.cidade
        else:
            cidade = Cidade.objects.get(id='5208707')
        request.session['cidade'] = cidade.id
    else:
        cidade = Cidade.objects.get(id=cidade)
    return cidade


@register.simple_tag
def cidades_disponiveis(request):
    options = []
    atual = cidade_atual(request)
    for c in Cinema.get_cidades_disponiveis():
        options.append("<option value='{0}' {3}>{1}/{2}</option>".format(c.id, c.nome, c.estado.sigla,
                                                                         "" if atual != c else "selected='selected'"))
    return mark_safe("\n".join(options))
