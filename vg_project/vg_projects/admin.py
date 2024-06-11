from django.contrib import admin
from .models import Perfildev

class Admin_Perfildev(admin.ModelAdmin):
    fields = ["imagen_perfil","nombre_perfil","correo_perfil","github_perfil","youtube_perfil" ,"twitch_perfil","facebook_perfil" ,"instagram_perfil","sobremi","archivo_proyecto","titulo_proyecto","descripcion_proyecto","categoria_proyecto"]
    list_display = ["nombre_perfil","sobremi","correo_perfil"]
admin.site.register(Perfildev,Admin_Perfildev)
