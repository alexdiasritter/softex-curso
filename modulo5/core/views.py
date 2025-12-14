from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):
    
    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Exercício 3: API de Estatísticas completa
class ContagemTarefasAPIView(APIView):
    
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        
        # Evitar divisão por zero
        taxa_conclusao = (concluidas / total) if total > 0 else 0.0

        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'taxa_conclusao': round(taxa_conclusao, 2)
        })