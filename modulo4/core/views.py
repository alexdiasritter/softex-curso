from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    
    """
    # passando uma variável através de context q é apenas um dict
    context: dict = {
        "name": "alex",
        "idade": 25
    }
    return render(request,'home.html', context=context)
    """
        
    my_context: dict = {
        "name": "Alex",
        "tecnologias": ['Python', 'Java', 'C', 'Javascript', 'HTML']
        }
    
    return render(request,'home.html', context=my_context)