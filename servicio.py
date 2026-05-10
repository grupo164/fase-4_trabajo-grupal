# Importación del decorador para métodos abstractos y entidad base del sistema
from abc import abstractmethod
from entidades_base import EntidadSistema

# Excepciones personalizadas del sistema
class ServicioError(Exception):
    pass

class CostoInvalidoError(ServicioError):
    pass

class ParametroInvalidoError(ServicioError):
    pass

# Clase abstracta que define la interfaz para los servicios
class Servicio(EntidadSistema):

    # Constructor que inicializa el nombre y costo base del servicio
    def __init__(self, nombre, costo_base):
        super().__init__(nombre)
        self.costo_base = costo_base

    # Método abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Método abstracto para describir el servicio específico en cada subclase
    @abstractmethod
    def describir_servicio(self):
        pass

    # Método abstracto para validar los parámetros de entrada necesarios
    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass

    # Método abstracto para mostrar detalles completos del servicio
    @abstractmethod
    def mostrar_detalles(self):
        pass

    # Método abstracto para validar el registro del servicio antes de su uso
    @abstractmethod
    def validar_registro(self):
        pass

    # Método para calcular el costo del servicio con impuesto
    def calcular_costo_con_impuesto(self, duracion, tasa_impuesto=0.19):
        costo = self.calcular_costo(duracion)
        return round(costo * (1 + tasa_impuesto), 2)

    # Método para calcular el costo del servicio con descuento
    def calcular_costo_con_descuento(self, duracion, descuento=0.0):
        costo = self.calcular_costo(duracion)
        return round(costo * (1 - descuento), 2)

    # Método para calcular el costo completo del servicio con impuesto y descuento
    def calcular_costo_completo(self, duracion, tasa_impuesto=0.19, descuento=0.0):
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