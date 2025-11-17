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
    
    # 1. Busca a tarefa pela 'pk' (ID) vinda da URL.
    # Se não achar, retorna um erro 404.
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':

        # 3. A Lógica de "Update"
        tarefa.concluida = True

        tarefa.save() # Não se esqueça de salvar!

        # 4. Redireciona de volta para a 'home' (Padrão PRG)
    return redirect('home')

def deletar_tarefa(request, pk):
    
    # 1. Busca a tarefa
    tarefa = get_object_or_404(Tarefa, pk=pk)

    # 2. Segurança: Apenas execute se o método for POST
    if request.method == 'POST':
        
        # 3. A Lógica de "Delete"
        tarefa.delete()

    # 4. Redireciona de volta para a 'home'
    return redirect('home')