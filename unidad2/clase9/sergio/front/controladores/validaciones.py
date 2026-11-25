import re
from datetime import datetime


class Validaciones():

    @staticmethod
    def validarTexto(valor, campo, maximo):
        texto = valor.strip()
        if not texto:
            return campo + ': falta este dato.'
        if len(texto) > maximo:
            return campo + ': admite máximo ' + str(maximo) + ' caracteres.'
        return None

    @staticmethod
    def validarEntero(valor, campo, minimo, maximo):
        texto = valor.strip()
        if not re.fullmatch('[0-9]+', texto) or not minimo <= int(texto) <= maximo:
            return campo + ': debe ser un entero entre ' + str(minimo) + ' y ' + str(maximo) + '.'
        return None

    @staticmethod
    def validarFecha(valor, campo):
        try:
            datetime.strptime(valor.strip(), '%Y-%m-%d')
        except ValueError:
            return campo + ': use el formato AAAA-MM-DD.'
        return None

    @staticmethod
    def validarPantalon(pantalon):
        errores = [
            Validaciones.validarTexto(pantalon.color.get(), 'color', 50),
            Validaciones.validarTexto(pantalon.material.get(), 'material', 50),
            Validaciones.validarTexto(pantalon.marca.get(), 'Marca', 50),
            Validaciones.validarEntero(pantalon.talla.get(), 'talla', 26, 50 ),
            Validaciones.validarFecha(pantalon.fecha_entrega.get(), 'Fecha de entrega'),
        ]
        return [error for error in errores if error]