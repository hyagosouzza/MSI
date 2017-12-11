from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from cinema.models import Sessao, Reserva, Cinema, Filme
from geo.models import Cidade
from dateutil.relativedelta import relativedelta
from interface.forms import LoginForm, CadastroForm, ReservaForm
from interface.templatetags.cidade import cidade_atual
from usuario.models import Usuario

REDIRECT_FIELD_NAME = "return"


def index(request):
    cidade = cidade_atual(request)
    ultima_data = timezone.now() + relativedelta(hours=1)
    sessoes = Sessao.objects.filter(cinema__cidade=cidade,
                                    data_horario__gte=ultima_data).order_by('data_horario')

    return render(request, 'interface/index.html', locals())


def cinemas(request):
    cidade = cidade_atual(request)
    cinemas = Cinema.objects.filter(cidade=cidade)
    return render(request, 'interface/cinemas.html', locals())


def log_out(request):
    logout(request)
    return redirect("/")


def log_in(request):
    erro = False
    msg = 'Informe seu usuário e senha'
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if request.GET.get(REDIRECT_FIELD_NAME):
                    return redirect(request.GET.get(REDIRECT_FIELD_NAME))
                else:
                    return redirect("/")
            erro = True
            msg = 'Usuário ou senha inválido. Tente novamente.'
    return render(request, "interface/login.html", locals())


def cadastrar(request):
    usuario = Usuario()
    form = CadastroForm(instance=usuario)
    if request.POST:
        form = CadastroForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['senha'])
            user.save()
            user = authenticate(email=user.username, password=form.cleaned_data['senha'])
            if user:
                login(request, user)
                return redirect("/")
    return render(request, "interface/cadastrar.html", locals())


def mudar_cidade(request):
    if request.POST and request.POST.get("cidade_atual"):
        cidade = get_object_or_404(Cidade, id=cidade_atual)
        request.session['cidade'] = cidade.id
    return JsonResponse({"sucesso": True})


@login_required(redirect_field_name="return", login_url="/login/")
def reservar(request, ident):
    sessao = get_object_or_404(Sessao, id=ident)
    reservas_realizadas = Reserva.objects.filter(sessao=sessao, usuario=request.user).exclude(status=2).aggregate(
        total=Sum("quantidade")).get("total") or 0
    disponivel = sessao.data_horario > timezone.now() + relativedelta(hours=1)
    if not disponivel:
        return render(request, 'interface/reservar.html', locals())
    reserva = Reserva(usuario=request.user, sessao=sessao)
    form = ReservaForm(instance=reserva)
    reserva_realizada = False
    if request.POST:
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save()
            reserva_realizada = True
    return render(request, 'interface/reservar.html', locals())


@login_required(redirect_field_name="return", login_url="/login/")
def reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by("-data_cadastro")
    if request.GET.get("cancelar"):
        reserva = get_object_or_404(Reserva, id=request.GET.get("cancelar"), usuario=request.user)
        reserva.status = 2
        reserva.save()
        return redirect(request.path)

    return render(request, 'interface/reservas.html', locals())
