from django.core.urlresolvers import reverse
from django.db.models import Model, CharField, ForeignKey, SlugField, BooleanField
from django.utils.translation import ugettext_lazy as _


class Pais(Model):
    class Meta:
        verbose_name = _(u'País')
        verbose_name_plural = _(u'Países')
        ordering = ('nome',)

    nome = CharField(_(u'Nome'), max_length=128)
    sigla = CharField(verbose_name=_(u'Sigla'),max_length=2)
    ativo = BooleanField(verbose_name=_(u'Ativo'), default=False)

    def __str__(self):
        return self.nome


class Estado(Model):
    class Meta:
        verbose_name = _(u'Estado')
        verbose_name_plural = _(u'Estados')
        ordering = ('nome',)

    pais = ForeignKey('Pais',verbose_name=_(u'País'),related_name='estado')
    nome = CharField(verbose_name=_(u'Nome'),max_length=80)
    sigla = CharField(verbose_name=_(u'Sigla'),max_length=2)
    # codigo = CharField(verbose_name=_(u'Código'), max_length=2, default=0)
    ativo = BooleanField(verbose_name=_(u'Ativo'), default=True)

    def __str__(self):
        return self.nome

    # def tem_parceiro(self):
    #     from parceiro.models import Parceiro
    #     if Parceiro.objects.filter(estado=self).exists():
    #         return True
    #     else:
    #         return False


class Cidade(Model):
    class Meta:
        verbose_name = _(u'Cidade')
        verbose_name_plural = _(u'Cidades')
        ordering = ('nome',)

    estado = ForeignKey('Estado',verbose_name=_(u'Estado'),related_name='cidade')
    nome = CharField(_(u'Nome'), max_length=60)
    ativo = BooleanField(verbose_name=_(u'Ativo'), default=True)

    def __str__(self):
        return self.nome

    def get_id_str(self):
        return str(self.id)

    # def tem_parceiro(self):
    #     from parceiro.models import Parceiro
    #     if Parceiro.objects.filter(cidade=self).exists():
    #         return True
    #     else:
    #         return False

