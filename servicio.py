from abc import ABC, abstractmethod

class Servicio(ABC):
    @abstractmethod
    def ejecutar(self):
        pass    