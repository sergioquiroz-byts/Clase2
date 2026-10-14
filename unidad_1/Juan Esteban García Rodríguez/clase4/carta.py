import tkinter as tk

class Carta():
    
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.fecha = tk.StringVar(ventana_principal)
        self.texto = tk.StringVar(ventana_principal)
        self.remitente = tk.StringVar(ventana_principal)
        self.destinatario = tk.StringVar(ventana_principal)
        self.direccion = tk.StringVar(ventana_principal)
