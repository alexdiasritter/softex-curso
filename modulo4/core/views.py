from typing import List
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404  
from .forms import TarefaForm
from .models import Tarefa
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User


@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST, user=request.user)
        if form.is_valid():
            tarefa = form.save(commit=False)  
            tarefa.user = request.user 
            tarefa.save()               
            return redirect('home')
    else:
        form = TarefaForm(user=request.user)
        username = request.user.username
    tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')
    context = {
        'nome_usuario': username,
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': tarefas,
        'form': form,
    }
    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
    return redirect('home')

@login_required
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
    return redirect('home')

def register(request):
    form = UserCreationForm(request.POST)
    print(form)
    if form.is_valid():
        user = form.save() 
        login(request, user)
        return redirect('home') 
    else:
        form = UserCreationForm() 
        context = {'form': form}
    return render(request, 'register.html', context)

def users(request):
    listUsers = User.objects.all()
    context = {
        'users': listUsers
    }
    return render(request, 'users.html', context=context)