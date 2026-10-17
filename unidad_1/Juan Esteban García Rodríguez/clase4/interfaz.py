import re
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkcalendar import DateEntry
from carta import Carta

class Interfaz():
    
    def __init__(self):
        self.ventana_principal = tk.Tk()
        
    def validar(self, fecha, texto, remitente, destinatario):
        #fecha:dd/mm/aaaa
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}",fecha):
            return "La fecha debe tener formato dd/mm/aaaa"
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{3,}", remitente):
            return "El remitente solo debe tener letras (minimo3)"
        if len(texto.strip()) < 5:
            return "El texto debe tener al menos 5 caracteres"
        return None   
        
    def accion_guardar_boton(self, carta, fecha, texto, remitente, destinatario):
        error = self.validar(fecha, texto, remitente, destinatario)
        if error:
            messagebox.showerror("Error de validación", error)
            return
        carta.fecha.set(fecha)
        carta.texto.set(texto)
        carta.remitente.set(remitente)
        carta.destinatario.set(destinatario)
        
        messagebox.showinfo(
            "guardar", 
            f"guardando: texto: {texto}"
            f"Fecha: {carta.fecha.get()}\n"
            f"Remitente: {carta.remitente.get()}\n"
            f"Destinatario: {carta.destinatario.get()}\n"
            f"Texto: {carta.texto.get()}"
        )
        
    def mostrar_interfaz(self):
        carta = Carta(self.ventana_principal)
        
        label_fecha = tk.Label(self.ventana_principal, text="Fecha")
        entry_fecha = DateEntry(self.ventana_principal,
                                textvariable=carta.fecha,
                                date_pattern="dd/mm/yyyy")
        
        label_remitente = tk.Label(self.ventana_principal, text="Remitente")
        entry_remitente = tk.Entry(self.ventana_principal,
                                   textvariable=carta.remitente)
        
        label_destinatario = tk.Label(self.ventana_principal, text="Destinatario")
        combo_destinatario = ttk.Combobox(self.ventana_principal,
                                          textvariable=carta.destinatario,
                                          values=["Mamá", "Papá", "Hermano", "Amigo", "Profesor"],
                                          state=("readonly"))
            
        label_Texto = tk.Label(self.ventana_principal, text="Texto")
        text_Texto = tk.Text(self.ventana_principal, height=5, width=30)
        
        boton_guardar = tk.Button(
            self.ventana_principal,
            text="guardar",
            command=lambda: self.accion_guardar_boton(
                carta,
                entry_fecha.get(),
                text_Texto.get("1.0", "end-1c"),
                entry_remitente.get(),
                combo_destinatario.get()))
            
        self.ventana_principal.title("Carta")
        self.ventana_principal.geometry("350x420")
            
        for widget in (label_fecha, entry_fecha,
                       label_remitente, entry_remitente,
                       label_destinatario, combo_destinatario,
                       label_Texto, text_Texto,
                       boton_guardar):
            widget.pack(pady=3)
        self.ventana_principal.mainloop()
