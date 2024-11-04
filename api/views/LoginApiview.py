from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Lógica para obtener el token
        response = super().post(request, *args, **kwargs)
        # Devolver solo el token
        return Response({'access': response.data['access'],
                          'refresh': response.data['refresh']}, status=status.HTTP_200_OK)

class CustomTokenRefreshView(TokenRefreshView):
    # Puedes personalizar la respuesta aquí si es necesario
    pass
