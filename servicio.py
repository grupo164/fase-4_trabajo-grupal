# Importación de la clase base abstracta y decorador para métodos abstractos
from abc import ABC, abstractmethod

# Clase abstracta que define la interfaz para los servicios
class Servicio(ABC):

    # Constructor que inicializa el nombre y costo base del servicio
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    # Método abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Método abstracto para validar parámetros del servicio
    @abstractmethod
    def validar_parametro(self):
        pass

    