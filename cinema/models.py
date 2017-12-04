from django.db import models
from django.utils import timezone

from cinema.choices import TIPOS_FILMES, CLASSIFICACAO


class Cinema(models.Model):
    class Meta:
        verbose_name = "Cinema"
        verbose_name_plural = "Cinemas"

    nome = models.CharField(verbose_name=u"Nome", max_length=50)
    endereco = models.CharField(verbose_name=u"Endereço", max_length=150)
    cidade = models.ForeignKey("geo.Cidade", verbose_name=u"Cidade")
    estado = models.ForeignKey("geo.Estado", verbose_name=u"Estado")
    data_cadastro = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now_add=True)
    data_alteracao = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now=True)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    categoria = models.ForeignKey("Categoria", verbose_name=u"Categoria")
    nome = models.CharField(verbose_name=u"Nome", max_length=50)
    imagem = models.ImageField(verbose_name="Imagem")
    descricao = models.TextField(verbose_name=u"Descrição")
    classificacao = models.PositiveSmallIntegerField(verbose_name=u"Classificação", choices=CLASSIFICACAO)
    duracao = models.DurationField(verbose_name=u"Duração")
    data_cadastro = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now_add=True)
    data_alteracao = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    nome = models.CharField(verbose_name=u"Nome", max_length=50)
    data_cadastro = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now_add=True)
    data_alteracao = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now=True)

    def __str__(self):
        return self.nome


class Sessao(models.Model):
    class Meta:
        verbose_name = "Sessão"
        verbose_name_plural = "Sessões"

    filme = models.ForeignKey("Filme", verbose_name=u"Filme")
    cinema = models.ForeignKey("Cinema", verbose_name=u"Cinema")
    preco = models.DecimalField(verbose_name=u"Preço", decimal_places=2, max_digits=9)
    quantidade = models.PositiveIntegerField(verbose_name=u"Quantidade de ingressos")
    data_horario = models.DateTimeField(verbose_name=u"Data e Horário")
    tipo = models.PositiveSmallIntegerField(verbose_name=u"Tipo", choices=TIPOS_FILMES)
    data_cadastro = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now_add=True)
    data_alteracao = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now=True)

    def __str__(self):
        return u"%s - %s" % (self.cinema, self.filme)


class Reserva(models.Model):
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    sessao = models.ForeignKey("Sessao", verbose_name=u"Sessão")
    usuario = models.ForeignKey("usuario.Usuario", verbose_name=u"Sessão")
    quantidade = models.PositiveIntegerField(verbose_name=u"Quantidade de reservas")
    data_cadastro = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now_add=True)
    data_alteracao = models.DateTimeField(verbose_name=u"Data de cadastro", auto_now=True)

    def __str__(self):
        return u"%s - %s" % (self.sessao, self.usuario)
