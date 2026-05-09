# Importación de la clase base abstracta, decorador para métodos abstractos y entidad base del sistema
from abc import ABC, abstractmethod
from entidades_base import EntidadSistema

# Clase abstracta que define la interfaz para los servicios
class Servicio(ABC, EntidadSistema):

    # Constructor que inicializa el nombre y costo base del servicio
    def __init__(self, nombre, costo_base):
        super().__init__(nombre)
        self.costo_base = costo_base

    # Método abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Método abstracto para validar parámetros del servicio
    @abstractmethod
    def validar_parametro(self):
        pass

    # Método para calcular el costo del servicio con impuesto
    def calcular_costo_con_impuesto(self, duracion, tasa_impuesto = 0.19):
        costo = self.calcular_costo(duracion)
        return round(costo * (1 + tasa_impuesto), 2)

    # Método para calcular el costo del servicio con descuento
    def calcular_costo_con_descuento(self, duracion, descuento = 0.0):
        costo = self.calcular_costo(duracion)
        return round(costo * (1 - descuento), 2)

    # Método para calcular el costo completo del servicio con impuesto y descuento
    def calcular_costo_completo(self, duracion, tasa_impuesto = 0.19, descuento = 0.0):
        subtotal = self.calcular_costo(duracion)
        valor_descuento = round(subtotal * descuento, 2)
        base_gravable = round(subtotal - valor_descuento, 2)
        valor_impuesto = round(base_gravable * tasa_impuesto, 2)
        total = round(base_gravable + valor_impuesto, 2)

        return {
           "servicio": self.nombre_entidad,
            "duracion_horas": duracion,
            "subtotal": subtotal,
            "descuento_aplicado": valor_descuento,
            "base_gravable": base_gravable,
            "impuesto": valor_impuesto,
            "total": total,
        }
