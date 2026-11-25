import re
import tkinter as tk
from datetime import datetime

class Pantalon():

    COLORES = ["Verde", "Negro", "Azul", "Café", "Blanco"]
    MATERIALES = ["Algodon", "Jean", "Cuero"]
    MARCAS = ["Levi's", "Wrangler", "Lee", "Dockers"]
    
    def __init__(self, ventana_principal):
        self.id = None
        self.ventana_principal = ventana_principal
        self.color = tk.StringVar(ventana_principal)
        self.talla = tk.StringVar(ventana_principal, value="32")
        self.material = tk.StringVar(ventana_principal)
        self.marca = tk.StringVar(ventana_principal)
        self.fecha_entrega = tk.StringVar(ventana_principal)

    def cargar(self, datos):
        self.id = datos['id']
        self.color.set(datos['color'])
        self.talla.set(datos['talla'])
        self.material.set(datos['material'])
        self.marca.set(datos['marca'])
        self.fecha_entrega.set(datos['fecha de entrega'])

    def limpiar(self):
        self.color.set('')
        self.talla.set('')
        self.material.set('')
        self.marca.set('')
        self.fecha_entrega.set('')

    def a_diccionario(self):
        return {
            'marca': self.marca.get().strip(),
            'talla': self.talla.get().strip(),
            'material': self.material.get().strip(),
            'fecha_creacion': self.fecha_entrega.get().strip(),
        }

    def validar(self):
        errores = []

        if self.color.get() not in self.COLORES:
            errores.append("Color: selecciona un color")

        talla = self.talla.get().strip()
        if not re.fullmatch(r"\d{2}", talla) or not 26 <= int(talla) <= 50:
            errores.append("Talla: debe ser un número entre 26 y 50.")

        if self.material.get() not in self.MATERIALES:
            errores.append("Material: selecciona una opción")

        if self.marca.get() not in self.MARCAS:
            errores.append("Marca: selecciona una marca")

        fecha = self.fecha_entrega.get().strip()
        try:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fecha):
                raise ValueError
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            errores.append("Formato de fecha inválido (use aaaa-mm-dd)")

        return errores


