from django.urls import path
from django.views import generic

from . import views
import os
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User

urlpatterns = [
     path('', views.login, name='login'),
     path('index', views.index, name='index'),
     path("logout/", LogoutView.as_view(), name="logout"),
     path('validar_usuario', views.validar_usuario, name='validar_usuario'),
     path('buscar_pokemon_api', views.buscar_pokemon_api, name='buscar_pokemon_api'),

     path('agregar_pokemon', views.agregar_pokemon, name='agregar_pokemon'),

     path('eliminar_pokemon', views.eliminar_pokemon, name='eliminar_pokemon'),

     path('registro', views.registro, name='registro'),


]