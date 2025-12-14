from django.urls import path
from .views import (
    ListaTarefasAPIView, 
    DetalheTarefaAPIView, 
    ContagemTarefasAPIView,
    DuplicarTarefaAPIView,
    ConcluirTodasTarefasAPIView
)

app_name = 'core'

urlpatterns = [
    # Coleção e Detalhe
    path('api/tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('api/tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    
    # Exercícios Extras
    path('api/tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('api/tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),
    
    # Estatísticas
    path('api/tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas')
]