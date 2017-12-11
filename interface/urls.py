from django.conf.urls import url
from django.conf.urls.static import static
from markseveriano import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^cadastrar/$', views.cadastrar, name='cadastrar'),
    url(r'^cinemas/$', views.cinemas, name='cinemas'),
    url(r'^reservas/$', views.reservas, name='reservas'),
    url(r'^reservar/(?P<ident>[\w_-]+)$', views.reservar, name='reservar'),
    url(r'^mudarCidade/$', views.mudar_cidade, name='reservar'),
    # url(r'^category', views.index_cat, name='index_cat'),
    # url(r'^tempestade', views.tempestade, name='tempestade'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
