from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Hola Mundo desde Django</h1>")
    return
def render(request, "otra.html")
    #return HttpResponse("<h1>Hola Mundo desde Django</h1>")
    return render(request, "otra.html")