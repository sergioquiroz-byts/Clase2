from datetime import date
from rest_framework import serializers
from pantalon.models.pantalon import Pantalon

class PantalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantalon
        fields = ["id", "marca", "talla", "fecha_creacion", "material"]

    def validate_marca(self, value):
        if not value.strip():
            raise serializers.ValidationError("La marca no puede estar vacía.")
        return value.strip()
    
    def validate_fecha_creacion(self, value):
        if value > date.today():
            raise serializers.ValidationError("ingrese una fecha valida.")
        return value
