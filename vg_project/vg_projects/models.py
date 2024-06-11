from django.db import models

# Create your models here.
class Desarrolladores(models.Model):
    iddev = models.AutoField(primary_key = True)
    correodev_1 = models.CharField(max_length = 100)
    telefonodev = models.IntegerField

class Clientes(models.Model):
    idcliente = models.AutoField(primary_key = True)
    nususario = models.CharField(max_length = 50)
    correou = models.CharField(max_length = 100)
    contraseña  = models.CharField(max_length = 50) 
    pagos = models.FloatField

class Perfildev(models.Model):
    idperfil = models.AutoField(primary_key = True)
    imagen_perfil  = models.ImageField(upload_to = 'imagen',blank = True)
    nombre_perfil  = models.CharField(max_length = 50,blank = True)
    correo_perfil  = models.CharField(max_length = 100,blank = True)
    github_perfil  = models.CharField(max_length = 100,blank = True)
    youtube_perfil  = models.CharField(max_length = 100,blank = True)
    twitch_perfil  = models.CharField(max_length = 100,blank = True)
    facebook_perfil  = models.CharField(max_length = 100,blank = True)
    instagram_perfil  = models.CharField(max_length = 100,blank = True)
    sobremi  = models.TextField(blank = True)
    archivo_proyecto = models.FileField(blank = True)
    titulo_proyecto  = models.CharField(max_length = 50)
    descripcion_proyecto  = models.TextField(blank = True)
    categoria_proyecto = models.CharField(max_length = 100)

class Comunidad(models.Model):
    id_comunidad = models.AutoField(primary_key = True)
    archivo_publicacion = models.FileField
    likes_publicacion = models.IntegerField
    comentarios_publicacion = models.TextField

class Finanzas(models.Model):
    idfinanzas = models.AutoField(primary_key = True)
    ganancia_dev = models.FloatField
    ganancia_pagina = models.FloatField