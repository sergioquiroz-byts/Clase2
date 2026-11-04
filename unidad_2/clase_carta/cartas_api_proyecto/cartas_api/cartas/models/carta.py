from django.db import models


class Carta(models.Model):
    fecha = models.DateField()
    texto = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"Carta de {self.remitente} para {self.destinatario}"
