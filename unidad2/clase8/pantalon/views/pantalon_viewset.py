from rest_framework.viewsets import ModelViewSet
from pantalon.models.pantalon import Pantalon
from pantalon.serializers.pantalon_serializer import PantalonSerializer
class PantalonViewSet(ModelViewSet):
    queryset = Pantalon.objects.all()
    serializer_class = PantalonSerializer
