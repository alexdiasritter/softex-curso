from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Olá mundo!</h1>") 

def house(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>This is our house</h1>")