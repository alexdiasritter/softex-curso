from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):
    def get(self, request):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TarefaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalheTarefaAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)

    def get(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Exercício 2: Endpoint de Duplicação
class DuplicarTarefaAPIView(APIView):
    def post(self, request, pk):
        tarefa_origem = get_object_or_404(Tarefa, pk=pk)
        
        # Cria cópia na memória
        tarefa_origem.pk = None
        tarefa_origem.titulo = f"{tarefa_origem.titulo} (Cópia)"
        tarefa_origem.concluida = False
        tarefa_origem.data_conclusao = None
        tarefa_origem.save()
        
        serializer = TarefaSerializer(tarefa_origem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Exercício 3: PATCH em Lote
class ConcluirTodasTarefasAPIView(APIView):
    def patch(self, request):
        # Atualiza todas as pendentes para concluídas
        atualizadas = Tarefa.objects.filter(concluida=False).update(concluida=True)
        return Response(
            {"mensagem": f"{atualizadas} tarefas foram concluídas com sucesso."},
            status=status.HTTP_200_OK
        )

class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        taxa = (concluidas / total) if total > 0 else 0
        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa, 2)
        })