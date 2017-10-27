from django.db import models
from django.utils import timezone

class Film(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50, default='link')
    url_img = models.CharField(max_length=300, default='.png')
    description = models.TextField()
    type = models.CharField(max_length=20, default='Dublado, 2D')
    faixa = models.CharField(max_length=300, default='.png')
    time = models.DurationField()
    director = models.CharField(max_length=30)
    elenco = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.name

class Categ(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    filme = models.ManyToManyField(Film)

    def __str__(self):
        return self.name

class Sessao(models.Model):
    id = models.AutoField(primary_key=True)
    filme = models.ManyToManyField(Film)
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    date = models.DateTimeField()
    cinema = models.CharField(max_length=50)
    shopping = models.CharField(max_length=50)
    cidade_uf = models.CharField(max_length=30, default='Cidade-UF')
    created_date = models.DateTimeField(
        default=timezone.now)

    def create(self):
        self.created_date =  timezone.now()
        self.save()

    def __str__(self):
        return self.title
