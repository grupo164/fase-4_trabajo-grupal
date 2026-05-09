# Importamos la clase Cliente para poder asociarla a la reserva
from gestion_clientes import Cliente

# Definimos la clase Reserva para gestionar la lógica de Software FJ
class Reserva:
    """
    Esta clase integra al cliente con el servicio y la duración.
    Implementa el manejo de excepciones para asegurar la estabilidad del sistema.
    """

    def __init__(self, cliente, servicio, duracion_horas):
        # Atributos básicos de una reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion_horas
        self.estado = "Pendiente"

    def procesar_confirmacion(self):
        """
        Lógica para confirmar la reserva usando bloques try-except (Manejo de errores).
        """
        try:
            print(f"Validando reserva para el cliente: {self.cliente.obtener_nombre()}")
            
            # Validación de seguridad: la duración no puede ser negativa o cero
            if self.duracion <= 0:
                # Si el dato es erróneo, lanzamos una excepción manualmente
                raise ValueError("La duración de la reserva debe ser mayor a 0 horas.")
            
            # Si todo está bien, confirmamos la reserva
            self.estado = "Confirmada"
            print(f"Éxito: Reserva confirmada por {self.duracion} horas.")

        except ValueError as error_dato:
            # Capturamos específicamente errores de valores incorrectos
            self.estado = "Error de Datos"
            print(f"No se pudo procesar la reserva: {error_dato}")
            # Se relanza el error para que sea capturado por el sistema de logs del compañero
            raise error_dato

        except Exception as e:
            # Capturamos cualquier otro error inesperado para evitar que el programa se cierre
            self.estado = "Error de Sistema"
            print(f"Ocurrió un fallo inesperado: {e}")
            raise e

    def cancelar(self):
        """Método para cambiar el estado de la reserva a cancelado"""
        self.estado = "Cancelada"
        print(f"La reserva de {self.cliente.obtener_nombre()} ha sido anulada.")
