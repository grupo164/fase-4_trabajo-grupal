# Importamos el módulo abc (Abstract Base Classes) necesario para crear abstracciones en Python
import abc

# Definimos la clase abstracta principal siguiendo el primer requerimiento de la guía
class EntidadSistema(abc.ABC):
    """
    Esta clase funciona como el plano maestro para Software FJ.
    Define que todos los objetos (Clientes, Servicios, etc.) deben tener un nombre y métodos de control.
    """

    # El constructor inicializa el atributo común para todas las entidades del sistema
    def __init__(self, nombre_entidad):
        # Asignamos el valor recibido al atributo de instancia
        self.nombre_entidad = nombre_entidad

    # Definimos el primer método abstracto obligatorio
    @abc.abstractmethod
    def mostrar_detalles(self):
        """
        Obliga a las clases hijas a implementar una función para mostrar su información.
        Esto asegura que el sistema siempre pueda imprimir reportes coherentes.
        """
        pass

    # Definimos el segundo método abstracto para validación (Requisito de robustez)
    @abc.abstractmethod
    def validar_registro(self):
        """
        Obliga a cada entidad a verificar que sus propios datos sean correctos.
        Esto es la base para el manejo de excepciones que pide la actividad.
        """
        pass
