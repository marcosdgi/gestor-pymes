from rest_framework.views import APIView

class EstadisticasApiView(APIView):
    def get(self, request): 
        year = request.GET