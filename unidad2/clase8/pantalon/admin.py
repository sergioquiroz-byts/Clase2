from django.contrib import admin
from pantalon.models.pantalon import Pantalon
@admin.register(Pantalon)
class PantalonAdmin(admin.ModelAdmin):
    list_display = ("id", "marca", "talla", "fecha_creacion", "material")
    search_fields = ("marca", "material")
    list_filter = ("talla", "material")
