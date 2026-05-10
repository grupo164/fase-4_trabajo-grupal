from servicio import Servicio

class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, capacidad_max):
        super().__init__(nombre, costo_base)
        self.capacidad_max = capacidad_max

    def calcular_costo(self, duracion):
        return round(self.costo_base * duracion, 2)

    def describir_servicio(self):
        return f"Sala: {self.nombre_entidad} | Capacidad: {self.capacidad_max} personas | Costo por hora: ${self.costo_base:,.0f}"

    def mostrar_detalles(self):
        return f"SERVICIO: {self.nombre_entidad} | Tipo: Reserva de Sala | Capacidad: {self._capacidad_max} personas"

    