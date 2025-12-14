from rest_framework import serializers
from datetime import date
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'prioridade', 'prazo', 'criada_em']
        read_only_fields = ['id', 'criada_em']

    def validate_titulo(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("O título não pode ser vazio ou conter apenas espaços.")
        if len(value) < 3:
            raise serializers.ValidationError("O título deve ter pelo menos 3 caracteres.")
        if value.isdigit():
            raise serializers.ValidationError("O título não pode conter apenas números.")
        return value

    # Exercício 2: Validação de Data (não pode ser no passado)
    def validate_prazo(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("O prazo não pode ser uma data no passado.")
        return value

    def validate(self, data):
        # Lógica para atualização parcial ou criação
        titulo = data.get('titulo', getattr(self.instance, 'titulo', '')).lower()
        concluida = data.get('concluida', getattr(self.instance, 'concluida', False))
        prazo = data.get('prazo', getattr(self.instance, 'prazo', None))

        # Validação da Aula (Urgente vs Concluída)
        if 'urgente' in titulo and concluida:
            raise serializers.ValidationError({
                "concluida": "Tarefas urgentes não podem ser criadas como concluídas."
            })

        # Exercício 2: Regra condicional de Prazo
        # Se concluida=False, prazo é obrigatório
        if not concluida and not prazo:
            raise serializers.ValidationError({
                "prazo": "O prazo é obrigatório para tarefas pendentes."
            })
            
        return data