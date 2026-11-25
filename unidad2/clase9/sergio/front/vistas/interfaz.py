import tkinter as tk
from tkinter import messagebox, ttk

from controladores.comunicacion import Comunicacion
from vistas.vista_pantalon import VistaPantalon


class Interfaz():

    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.comunicacion = Comunicacion()

    def al_cambiar_pestana(self, evento):
        pestana = self.pestanas.nametowidget(self.pestanas.select())
        if hasattr(pestana, 'refrescar'):
            pestana.refrescar()

    def al_cerrar(self):
        if messagebox.askyesno('Salir', '¿Seguro que quieres cerrar la aplicación?', parent=self.ventana_principal):
            self.ventana_principal.destroy()

    def mostrar_interfaz(self):
        self.ventana_principal.title('Gestión de Pantalones')
        self.ventana_principal.geometry('900x600')
        self.ventana_principal.minsize(820, 520)

        self.pestanas = ttk.Notebook(self.ventana_principal)
        self.pestanas.add(VistaPantalon(self.pestanas, self.comunicacion), text='Pantalones')
        self.pestanas.pack(fill='both', expand=True)
        self.pestanas.bind('<<NotebookTabChanged>>', self.al_cambiar_pestana)

        self.ventana_principal.protocol('WM_DELETE_WINDOW', self.al_cerrar)
        self.ventana_principal.mainloop()
