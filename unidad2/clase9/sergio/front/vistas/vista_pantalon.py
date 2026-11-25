import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from controladores.comunicacion import ErrorComunicacion
from controladores.validaciones import Validaciones
from modelos.Pantalon import Pantalon
from vistas.vista_base import VistaBase


class VistaPantalon(VistaBase):

    titulo_formulario = 'Datos del Pantalón'
    recurso = 'pantalones'
    columnas = (
        ('id', 'Id', 40),
        ('color', 'Color', 130),
        ('talla', 'Talla', 60),
        ('material', 'Material', 120),
        ('marca', 'Marca', 120),
        ('fecha_entrega', 'Fecha de Entrega', 120),
        ('comprado', 'Comprado', 80),
    )

    def crear_modelo(self):
        return Pantalon(self)

    def construir_campos(self, marco):
        marco.columnconfigure(1, weight=1)
        marco.columnconfigure(3, weight=1)

        combo_color = ttk.Combobox(marco, textvariable=self.modelo.color, values=Pantalon.COLORES, state="readonly")
        spin_talla = tk.Spinbox(marco, from_=26, to=50, textvariable=self.modelo.talla)
        combo_material = ttk.Combobox(marco, textvariable=self.modelo.material, values=Pantalon.MATERIALES, state="readonly")
        combo_marca = ttk.Combobox(marco, textvariable=self.modelo.marca, values=Pantalon.MARCAS, state="readonly")
        entry_fecha = DateEntry(marco, textvariable=self.modelo.fecha_entrega, date_pattern="yyyy-mm-dd", state="readonly")

        ttk.Label(marco, text='Color').grid(row=0, column=0, sticky='w', pady=4, padx=(0, 8))
        combo_color.grid(row=0, column=1, sticky='ew', pady=4, padx=(0, 16))
        ttk.Label(marco, text='Talla (26 a 50)').grid(row=0, column=2, sticky='w', pady=4, padx=(0, 8))
        spin_talla.grid(row=0, column=3, sticky='ew', pady=4)
        ttk.Label(marco, text='Material').grid(row=1, column=0, sticky='w', pady=4, padx=(0, 8))
        combo_material.grid(row=1, column=1, sticky='ew', pady=4, padx=(0, 16))
        ttk.Label(marco, text='Marca').grid(row=1, column=2, sticky='w', pady=4, padx=(0, 8))
        combo_marca.grid(row=1, column=3, sticky='ew', pady=4)
        ttk.Label(marco, text='Fecha de entrega').grid(row=2, column=0, sticky='w', pady=4, padx=(0, 8))
        entry_fecha.grid(row=2, column=1, sticky='ew', pady=4, padx=(0, 16))

        if hasattr(self.modelo, 'comprado'):
            check_comprado = ttk.Checkbutton(marco, text='Comprado', variable=self.modelo.comprado)
            check_comprado.grid(row=2, column=2, columnspan=2, sticky='w', pady=4)

    def crear_botones(self):
        super().crear_botones()
        if hasattr(self.modelo, 'comprado'):
            self.boton_estado = ttk.Button(
                self.boton_limpiar.master,
                text='Confirmar compra',
                command=self.accion_cambiar_estado,
                state='disabled'
            )
            self.boton_estado.pack(side='left', padx=(24, 0))

    def actualizar_botones(self):
        super().actualizar_botones()
        if hasattr(self, 'boton_estado'):
            registro = self.registros.get(self.modelo.id)
            if registro is None:
                self.boton_estado.state(['disabled'])
            else:
                self.boton_estado.state(['!disabled'])
                self.boton_estado.config(text='No comprado' if registro.get('comprado') else 'Confirmar compra')

    def accion_cambiar_estado(self):
        registro = self.registros[self.modelo.id]
        cambio = {'comprado': not registro.get('comprado', False)}
        try:
            self.comunicacion.modificar(self.recurso, registro['id'], cambio)
        except ErrorComunicacion as error:
            messagebox.showerror('No se pudo cambiar el estado', str(error))
            return
        self.refrescar('Compra confirmada.' if cambio['comprado'] else 'Marcado como no comprado.')

    def validar(self):
        return Validaciones.validarPantalon(self.modelo)

    def datos_formulario(self):
        return self.modelo.a_diccionario()

    def valores_fila(self, registro):
        return (
            registro.get('id', ''),
            registro.get('color', ''),
            registro.get('talla', ''),
            registro.get('material', ''),
            registro.get('marca', ''),
            registro.get('fecha_entrega', ''),
            'Sí' if registro.get('comprado') else 'No',
        )

    def texto_confirmar_eliminar(self, registro):
        return f"¿Eliminar el pantalón {registro.get('marca', '')} ({registro.get('color', '')}, talla {registro.get('talla', '')})?"
