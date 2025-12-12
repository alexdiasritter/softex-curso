from django.urls import path
from .views import ContagemTarefasAPIView, ListaTarefasAPIView

# Namespace do app (útil para reverse())
app_name = 'core'
urlpatterns = [
    # /api/tarefas/ → ListaTarefasAPIView
    path('api/tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('api/tarefas/contagem', ContagemTarefasAPIView.as_view(), name='contagem-tarefas')
    ]
