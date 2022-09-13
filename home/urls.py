from unicodedata import name

from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("escrever/", views.escrever, name='escrever'),
    path("cadastrar/", views.cadastrar_user, name='cadastrar'),
    path("logar/", views.logar_user, name='logar'),
    path("sair/", views.sair_user, name='sair'),
]