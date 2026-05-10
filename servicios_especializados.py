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

    def validar_parametros(self, **kwargs):
        duracion = kwargs.get("duracion")
        if duracion is None or duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0.")
        num_asistentes = kwargs.get("num_asistentes")
        if num_asistentes is not None and num_asistentes > self._capacidad_max:
            raise ValueError(f"Los asistentes ({num_asistentes}) superan la capacidad máxima ({self._capacidad_max}).")
        return True

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, tipo_equipo, cantidad_disponible):
        super().__init__(nombre, costo_base)
        self.tipo_equipo = tipo_equipo
        self.cantidad_disponible = cantidad_disponible
    
    def calcular_costo(self, duracion):
        return round(self.costo_base * duracion * self.cantidad_disponible, 2)

    def describir_servicio(self):
        return f"Equipo: {self.nombre_entidad} | Tipo: {self._tipo_equipo} | Stock: {self._cantidad_disponible} | Costo por hora: ${self.costo_base:,.0f}"

    def mostrar_detalles(self):
        return f"SERVICIO: {self.nombre_entidad} | Tipo: Alquiler de Equipo | Stock: {self._cantidad_disponible}"

    def validar_registro(self):
        if not self.nombre_entidad or self.costo_base <= 0 or not self._tipo_equipo:
            raise ValueError("Datos del equipo inválidos.")
 
    def validar_parametros(self, **kwargs):
        duracion = kwargs.get("duracion")
        if duracion is None or duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0.")
        cantidad = kwargs.get("cantidad", 1)
        if cantidad > self._cantidad_disponible:
            raise ValueError(f"Cantidad solicitada ({cantidad}) supera el stock disponible ({self._cantidad_disponible}).")
        return True