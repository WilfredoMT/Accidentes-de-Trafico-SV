from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index de Inicio de seccion.")

def home(request):
    return render(request,"paginaLogin/home.html")
