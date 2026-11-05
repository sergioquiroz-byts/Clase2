from django.db import models
class Pantalon(models.Model):
    marca = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    material = models.CharField(max_length=50)
    class Meta:
        ordering = ["id"]
        verbose_name = "Pantalón"
        verbose_name_plural = "Pantalones"
    def __str__(self):
        return f"{self.marca} - talla {self.talla}"
