from rest_framework import serializers
from cartas.models import Carta


class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = [
            "id",
            "fecha",
            "texto",
            "remitente",
            "destinatario",
            "direccion",
        ]

    # Validamos que el remitente tenga al menos 3 caracteres.
    def validate_remitente(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError(
                "El nombre del remitente debe tener al menos 3 caracteres."
            )
        return value
