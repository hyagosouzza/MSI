from django.shortcuts import render
from django.utils import timezone
from .models import Film, Categ

# Create your views here.
def index(request):
    name = Film.objects.order_by('created_date')
    #ses = Sessao.objects.datetimes('date', 'second', order='DESC')
    return render(request, 'msi/index.html', {'index': name})

def index_title(request):
    name = Film.objects.order_by('name')
    return render(request, 'msi/index_title.html', {'index': name})

def index_cat(request):
    categ = Categ.objects.order_by('name')
    return render(request, 'msi/index_cat.html', {'index_cat': categ})

def tempestade(request):
    temp_film = Film.objects.get(link="tempestade")
    return render(request, 'msi/tempestade.html', {'tempestade': temp_film})
