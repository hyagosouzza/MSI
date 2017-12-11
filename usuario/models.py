from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, EmailField, CharField, ForeignKey
from django.utils.translation import ugettext_lazy as _


class Usuario(AbstractUser):
    class Meta:
        verbose_name = _(u'Usuario')
        verbose_name_plural = _(u'Usuario')

    first_name = CharField(verbose_name=u"Primeiro Nome", null=False, blank=False, max_length=150)
    email = EmailField(verbose_name=u"Email", null=False, blank=False)
    cidade = ForeignKey("geo.Cidade", verbose_name="Cidade", default="5208707")

    def __str__(self):
        return str(self.username)
