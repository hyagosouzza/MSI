from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^title', views.index_title, name='index_title'),
    # url(r'^category', views.index_cat, name='index_cat'),
    # url(r'^tempestade', views.tempestade, name='tempestade'),
]