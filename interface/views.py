from django.shortcuts import render
from django.utils import timezone
from cinema.models import Sessao


def index(request):
    name = Sessao.objects.order_by('data_cadastro')
    return render(request, 'interface/index.html', {'index': name})

#
# def index_title(request):
#     name = Film.objects.order_by('name')
#     return render(request, 'interface/index_title.html', {'index': name})
#
# def index_cat(request):
#     categ = Categ.objects.order_by('name')
#     return render(request, 'interface/index_cat.html', {'index_cat': categ})
#
# def tempestade(request):
#     temp_film = Film.objects.get(link="tempestade")
#     return render(request, 'interface/tempestade.html', {'tempestade': temp_film})
