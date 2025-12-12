from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView): 
    
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
                    
class ContagemTarefasAPIView(APIView):
    
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        return Response({
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes
        })