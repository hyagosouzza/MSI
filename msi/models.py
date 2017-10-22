from django.db import models
from django.utils import timezone

# Create your models here.
class Sessao(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=30)
    type = models.CharField(max_length=30, default='Dublado, 2D')
    faixa = models.IntegerField(default=0)
    time = models.DurationField()
    date = models.DateTimeField()
    cinema = models.CharField(max_length=30)
    shopping = models.CharField(max_length=30)
    cidade_uf = models.CharField(max_length=30, default='Cidade-UF')
    director = models.CharField(max_length=30)
    elenco = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def create(self):
        self.created_date =  timezone.now()
        self.save()

    def __str__(self):
        return self.title