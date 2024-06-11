from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"base.html")

def inicio(request):
    return render (request,"inicio.html")

def perfil(request):
    return render(request,"perfil.html")

def pago(request):
    return render(request,"pago.html")

def categorias(request):
    return render(request,"categorias.html")

def comunidad(request):
    return render(request,"comunidad.html")

def base(request):
    return render(request,"base.html")

def Logup(request):
    return render(request,"logup.html")

def Login(request):
    return render(request,"login.html")

def resultado(request):
    return render(request,"resultado_usuario.html")

def reclutamiento(request):
    return render(request,"reclutamiento.html")