from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404  
from .forms import TarefaForm
from .models import Tarefa

def home(request):
    tarefas = Tarefa.objects.all().order_by('-criada_em')
    
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = TarefaForm()
        
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': tarefas,
        'form': form,
    }
    return render(request, 'home.html', context)

def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
    return redirect('home')

def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
    return redirect('home')