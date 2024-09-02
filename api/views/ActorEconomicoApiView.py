from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.ActorEconomicoSerializer import ActorEconomicoSerializer
from api.models.ActorEconomico import ActorEconomico
from rest_framework import status

class ActorEconomicoApiView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                actor = ActorEconomico.objects.get(id=pk)
                actor_serializer = ActorEconomicoSerializer(actor, many=False)
                return Response(actor_serializer.data, status=status.HTTP_200_OK)
            except ActorEconomico.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            actores = ActorEconomico.objects.all()
            actor_serializer = ActorEconomicoSerializer(actores, many=True)
            return Response(actor_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActorEconomicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id = None):
        if id is not None:
            actor = ActorEconomico.objects.get(id=id)
            serializer = ActorEconomicoSerializer(actor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id = None):
        if id is not None:
            actor = ActorEconomico.objects.get(id=id)
            if actor:
                actor.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

def getByNumero(request):
    if request.method == 'GET':
        numero = request.GET.get('numero')  
        print(numero)
        actor = ActorEconomico.objects.get(numero=numero)
        serializer = ActorEconomicoSerializer(actor, many=false)
        return Response(serializer.data, status=status.HTTP_200_OK)