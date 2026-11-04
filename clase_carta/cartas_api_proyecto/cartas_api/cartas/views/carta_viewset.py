from rest_framework import viewsets
from cartas.models import Carta
from cartas.serializers import CartaSerializer


class CartaViewSet(viewsets.ModelViewSet):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer
