from rest_framework import serializers
from django.utils import timezone
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'prioridade', 'prazo', 'data_conclusao', 'criada_em']
        read_only_fields = ['id', 'criada_em', 'data_conclusao'] # data_conclusao é automático

    def validate(self, data):
        # Lógica para pegar valor novo ou manter o antigo
        titulo = data.get('titulo', getattr(self.instance, 'titulo', '')).lower()
        concluida_nova = data.get('concluida', getattr(self.instance, 'concluida', False))
        prioridade = data.get('prioridade', getattr(self.instance, 'prioridade', 'media'))

        # Exercício 4: Tarefas 'alta' só podem ser concluídas via PUT
        request = self.context.get('request')
        if request and request.method == 'PATCH':
            if prioridade == 'alta' and concluida_nova is True:
                # Verifica se ela já não estava concluída antes
                if not getattr(self.instance, 'concluida', False):
                    raise serializers.ValidationError(
                        "Tarefas de alta prioridade exigem revisão completa (PUT) para serem concluídas."
                    )

        # Validação de Urgência (da aula anterior)
        if 'urgente' in titulo and concluida_nova:
            raise serializers.ValidationError("Tarefas urgentes não podem ser criadas como concluídas.")

        return data

    def update(self, instance, validated_data):
        # Exercício 1: Lógica de preenchimento/limpeza da data_conclusao
        concluida_anterior = instance.concluida
        concluida_nova = validated_data.get('concluida', concluida_anterior)

        if not concluida_anterior and concluida_nova:
            # Está concluindo agora -> marca data
            instance.data_conclusao = timezone.now()
        elif concluida_anterior and not concluida_nova:
            # Está reabrindo -> limpa data
            instance.data_conclusao = None
            
        return super().update(instance, validated_data)