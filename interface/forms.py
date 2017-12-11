import re

from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm, CheckboxInput

from cinema.models import Reserva
from usuario.models import Usuario


class BaseBoostrapForm(object):
    def __init__(self, *args, **kwargs):
        super(BaseBoostrapForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            if isinstance(self.fields[f].widget, CheckboxInput):
                attr_class = self.fields[f].widget.attrs.get("class", "")
                attr_class += " filled-in"
                self.fields[f].widget.attrs["class"] = attr_class
                setattr(self[f], "is_checkbox", True)
            else:
                attr_class = self.fields[f].widget.attrs.get("class", "")
                attr_class += " form-control form-control-line"
                self.fields[f].widget.attrs["class"] = attr_class
                setattr(self[f], "is_checkbox", False)
                self.fields[f].widget.attrs["placeholder"] = self.fields[f].label


class LoginForm(BaseBoostrapForm, Form):
    class Meta:
        fields = ("username", "password", 'captcha')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'

    username = CharField(label=u"Usuário", required=True, max_length=90,
                         widget=TextInput(attrs={'placeholder': 'Usuário'}))
    password = CharField(label=u"Senha", required=True, max_length=60, min_length=3,
                         widget=PasswordInput(attrs={'placeholder': 'Senha'}))


class CadastroForm(BaseBoostrapForm, ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'first_name', 'last_name', 'username', 'email', 'senha', 'confirme'
        )

    senha = CharField(label=u"Senha", required=True, max_length=60, min_length=6,
                      help_text=u"Necessário no mínimo 6 caracteres, contendo ao menos uma letra e um número.",
                      widget=PasswordInput())
    confirme = CharField(label=u"Confirme a senha", required=True, max_length=60, widget=PasswordInput())

    def clean_senha(self):
        password = self.cleaned_data['senha']
        if re.search(r'[a-z]', password, re.IGNORECASE) is None:
            raise ValidationError("Sua senha deve conter ao menos uma letra.")
        if re.search(r'\d', password, re.IGNORECASE) is None:
            raise ValidationError("Sua senha deve conter ao menos um número.")
        return password

    def clean_confirme(self):
        password = self.cleaned_data.get('senha', None)
        confirme = self.cleaned_data.get('confirme', None)
        if password is not None and password != confirme:
            raise ValidationError("Senhas diferentes")
        return confirme


class ReservaForm(BaseBoostrapForm, ModelForm):
    class Meta:
        model = Reserva
        fields = (
            'quantidade',
        )

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade', 0)
        disponivel = self.instance.sessao.quantidade - (
            Reserva.objects.filter(sessao=self.instance.sessao).exclude(status=2).aggregate(
                total=Sum("quantidade")).get(
                "total") or 0)
        if quantidade == 0 or quantidade > disponivel:
            raise ValidationError("Quantidade informada não está disponível para reserva")
        return quantidade
