from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

# --- VISTAS BASADAS EN FUNCIONES ---

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def mock_predict_text(request):
    """
    Endpoint temporal (Mock) para simular la predicción de la RNN.
    """
    # Capturamos la palabra o frase que envíe Flutter
    input_text = request.data.get('text', '')

    # Respuesta simulada (Mock) según tu lógica de negocio
    mock_suggestions = ["agua", "descansar", "ayuda"]

    return Response({
        "input_received": input_text,
        "predictions": mock_suggestions,
        "status": "success (authenticated, mocked)"
    })


# --- VISTAS BASADAS EN CLASES ---

class RegisterView(generics.CreateAPIView):
    """
    Servicio de registro para nuevos usuarios (Auth Service).
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer