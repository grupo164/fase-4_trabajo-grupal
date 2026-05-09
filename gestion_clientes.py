# Importamos la base que creaste para aplicar herencia
from entidades_base import EntidadSistema

# Definimos la clase Cliente cumpliendo con los requisitos de la actividad
class Cliente(EntidadSistema):
    """
    Gestiona los datos de los usuarios de Software FJ.
    Aplica encapsulamiento (atributos privados) y validación de datos.
    """

    def __init__(self, nombre, identificacion, correo):
        # Inicializamos la clase padre con el nombre
        super().__init__(nombre)
        # Atributos privados con doble guion bajo (Encapsulamiento)
        self.__identificacion = identificacion
        self.__correo = correo
        # Ejecutamos validación inmediata al crear el objeto
        self.validar_registro()

    def validar_registro(self):
        """
        Verifica que no existan campos vacíos para garantizar la robustez.
        """
        if not self.nombre_entidad or not self.__identificacion or not self.__correo:
            # Si falta información, lanzamos una excepción de valor
            raise ValueError("Error: Todos los datos del cliente son obligatorios.")

    def mostrar_detalles(self):
        """
        Implementa el método abstracto para mostrar la ficha del cliente.
        """
        return f"CLIENTE: {self.nombre_entidad} | ID: {self.__identificacion}"

    # Método público para obtener el nombre del cliente de forma segura
    def obtener_nombre(self):
        return self.nombre_entidad
