from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Tarefa


def home(request):
    tarefas = Tarefa.objects.all()
    context = {
        'nome_usuario': 'alex',
        'tecnologias': ['Python, Java, Django, Models'],
        'tarefas': tarefas
    }
    return render(request, 'home.html', context)







'''
def home(request: HttpRequest) -> HttpResponse:
        
    my_context: dict = {
        "name": "Alex",
        "tecnologias": ['Python', 'Java', 'C', 'Javascript', 'HTML']
        }
    
    return render(request,'home.html', context=my_context)
'''