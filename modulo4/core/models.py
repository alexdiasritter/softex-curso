from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Tarefa(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255, default='')
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tarefas')
    
    def __str__(self):
        return self.titulo
    