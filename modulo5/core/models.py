from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tarefas',
        verbose_name='Usuário'
    )
    titulo = models.CharField(max_length=200, verbose_name='Título')
    concluida = models.BooleanField(default=False, verbose_name='Concluída')
    
    # Exercício 1: Campo de Prioridade
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
        verbose_name='Prioridade'
    )
    
    # Exercício 2: Campo de Prazo
    prazo = models.DateField(
        null=True, 
        blank=True, 
        verbose_name='Prazo de Conclusão'
    )
    
    criada_em = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']