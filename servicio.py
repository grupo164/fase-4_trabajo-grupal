from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costos(self):
        pass

    @abstractmethod
    def describir_servicios(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass