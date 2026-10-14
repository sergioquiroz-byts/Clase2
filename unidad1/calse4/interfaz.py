import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from Pantalon import Pantalon

class Interfaz():

    def __init__(self):
        self.ventana_principal = tk.Tk()

    def accion_guardar_boton(self, pantalon):
        errores = pantalon.validar()
        if errores:
            messagebox.showerror("Error de validación", "\n".join(errores),
                                 parent=self.ventana_principal)
            return


        messagebox.showinfo(
            "Guardar compra",
            "Datos guardados correctamente:\n\n"
            f"Color: {pantalon.color.get()}\n"
            f"Talla: {pantalon.talla.get()}\n"
            f"Material: {pantalon.material.get()}\n"
            f"Marca: {pantalon.marca.get()}\n"
            f"Fecha de entrega: {pantalon.fecha_entrega.get()}",
            parent=self.ventana_principal
        )


    def mostrar_interfaz(self) :
        pantalon = Pantalon(self.ventana_principal)

        #Color
        label_color = tk.Label(self.ventana_principal, text="Color")
        combo_color = ttk.Combobox(self.ventana_principal,
                                   textvariable=pantalon.color,
                                   values=Pantalon.COLORES, state="readonly")

        #Talla
        label_talla = tk.Label(self.ventana_principal, text="Talla")
        spin_talla = tk.Spinbox(self.ventana_principal, from_=26, to=50,
                                textvariable=pantalon.talla)

        #Material
        label_material = tk.Label(self.ventana_principal, text="Material")
        combo_material = ttk.Combobox(self.ventana_principal,
                                      textvariable=pantalon.material,
                                      values=Pantalon.MATERIALES, state="readonly")

        #Marca
        label_marca = tk.Label(self.ventana_principal, text="Marca")
        combo_marca = ttk.Combobox(self.ventana_principal,
                                   textvariable=pantalon.marca,
                                   values=Pantalon.MARCAS, state="readonly")

        #Fecha compra 
        label_fecha = tk.Label(self.ventana_principal, text="Fecha de entrega")
        entry_fecha = DateEntry(self.ventana_principal,
                                textvariable=pantalon.fecha_entrega,
                                date_pattern="dd/mm/yyyy", state="readonly")

        #Boton
        boton_guardar = tk.Button(
            self.ventana_principal, text="Guardar compra",
            command=lambda: self.accion_guardar_boton(pantalon))
        

        self.ventana_principal.title("Ventana Principal")
        self.ventana_principal.geometry("380x400")

        label_color.pack(pady=3)
        combo_color.pack()
        label_talla.pack(pady=3)
        spin_talla.pack()
        label_material.pack(pady=3)
        combo_material.pack()
        label_marca.pack(pady=3)
        combo_marca.pack()
        label_fecha.pack(pady=3)
        entry_fecha.pack()
        boton_guardar.pack(pady=20)

        self.ventana_principal.mainloop()