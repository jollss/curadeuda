from django.db import models

# Create your models here.
class crear_pokemones(models.Model):
    nombre  = models.CharField(max_length=150,null=True,blank=True)
    foto= models.CharField(max_length=255,null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_pokemon = models.CharField(max_length=3,null=True,blank=True)
