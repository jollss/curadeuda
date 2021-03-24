from django.shortcuts import render, redirect
import os
import os.path
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.models import *
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
import requests,json
from django.contrib.auth.hashers import make_password

from upokemon.models import *
# Create your views here.


def login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username='jollss', password=password)
        if user is not None:
            id=request.session["id"] = user.id
            nombre=request.session["usuario"] = user.username
            correo=request.session["correo"] = user.email
            all_pokemones = crear_pokemones.objects.all().values("id","nombre","foto","id_pokemon")     
            

            return render(
            request,
            'inicio/responsive_table.html',
            #'inicio/inicio.html',
            context={'id':id,'nombre':nombre,'correo':correo,'all_pokemones':all_pokemones},
            )            
    else:
        return render(
        request,
        'inicio/index.html',
        context={},
    )

def buscar_pokemon_api(request):
            nombre_pokemon=request.POST.get('nombre')
            url="https://pokeapi.co/api/v2/pokemon/"+nombre_pokemon
            response=requests.get(url)
            if response.status_code == 200:
                b=json.loads(response.content)
                datos=b['sprites']['front_default']
                return HttpResponse(json.dumps({'idpokemon':b['id'],'img':datos,'nombre':nombre_pokemon}), content_type='aplication/json')

            else:
                return HttpResponse(json.dumps("400"), content_type='aplication/json')

def agregar_pokemon(request):
    idpokemon=request.POST.get('id_pokemon')
    url="https://pokeapi.co/api/v2/pokemon/"+idpokemon
    response=requests.get(url)
    if response.status_code == 200:
        b=json.loads(response.content)
        nombre=b['species']['name']
        foto=b['sprites']['front_default']
        cre_pokemon=crear_pokemones()
        cre_pokemon.id_pokemon=idpokemon
        cre_pokemon.foto=foto
        cre_pokemon.nombre=nombre
        cre_pokemon.save()
    return HttpResponse(json.dumps("agregado"), content_type='aplication/json')





def index(request):
    pass
    """return render(
                request,
                'inicio.html',
                context={},
            )"""

def eliminar_pokemon(request):
    instance = crear_pokemones.objects.get(id=request.POST.get('id')) 
    instance.delete()
    return HttpResponse(json.dumps("eliminado"), content_type='aplication/json')

def validar_usuario(request):

    user= User.objects.filter(username=request.POST.get('nombre')).exists()
    if user is True:
        valor="True"
    else:
        valor="False"
    return HttpResponse(json.dumps(valor), content_type='aplication/json')

def registro(request):
    try:
        contra=make_password(request.POST.get('password'))

        crear_usuario=User()
        crear_usuario.username=request.POST.get('nombre')
        crear_usuario.email=request.POST.get('correo')
        crear_usuario.password=contra
        crear_usuario.save()
        
        return render(
            request,
            'inicio/index.html',
            context={'valor':"Usuario Registrado correctamente"},
        )
    except:
        return render(
            request,
            'inicio/index.html',
            context={},
        )


class SignOutView(LogoutView):
    pass