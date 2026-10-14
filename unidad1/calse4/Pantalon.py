import re
import tkinter as tk
from datetime import datetime

class Pantalon():

    COLORES = ["Verde", "Negro", "Azul", "Café", "Blanco"]
    MATERIALES = ["Algodon", "Jean", "Cuero"]
    MARCAS = ["Levi's", "Wrangler", "Lee", "Dockers"]
    
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.color = tk.StringVar(ventana_principal)
        self.talla = tk.StringVar(ventana_principal, value="32")
        self.material = tk.StringVar(ventana_principal)
        self.marca = tk.StringVar(ventana_principal)
        self.fecha_entrega = tk.StringVar(ventana_principal)


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
            if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", fecha):
                raise ValueError
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            errores.append("formato dd/mm/aaaa invalido")

        return errores



