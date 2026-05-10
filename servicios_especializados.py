from servicio import Servicio


class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, capacidad_max):
        super().__init__(nombre, costo_base)
        self._capacidad_max = capacidad_max

    def calcular_costo(self, duracion):
        return round(self.costo_base * duracion, 2)

    def describir_servicio(self):
        return f"Sala: {self.nombre_entidad} | Capacidad: {self._capacidad_max} personas | Costo por hora: ${self.costo_base:,.0f}"

    def mostrar_detalles(self):
        return f"SERVICIO: {self.nombre_entidad} | Tipo: Reserva de Sala | Capacidad: {self._capacidad_max} personas"

    def validar_registro(self):
        if not self.nombre_entidad or self.costo_base <= 0 or self._capacidad_max <= 0:
            raise ValueError("Datos de la sala inválidos.")

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
        self._tipo_equipo = tipo_equipo
        self._cantidad_disponible = cantidad_disponible

    def calcular_costo(self, duracion):
        return round(self.costo_base * duracion * self._cantidad_disponible, 2)

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


class AsesoriaEspecializada(Servicio):

    MULTIPLICADORES = {"junior": 1.0, "senior": 1.5, "principal": 2.0}

    def __init__(self, nombre, costo_base, area, nivel_experto):
        super().__init__(nombre, costo_base)
        self._area = area
        self._nivel_experto = nivel_experto.lower()
        self._multiplicador = self.MULTIPLICADORES.get(self._nivel_experto, 1.0)

    def calcular_costo(self, duracion):
        return round(self.costo_base * duracion * self._multiplicador, 2)

    def describir_servicio(self):
        return f"Asesoría: {self.nombre_entidad} | Área: {self._area} | Nivel: {self._nivel_experto} | Costo por hora: ${self.costo_base:,.0f}"

    def mostrar_detalles(self):
        return f"SERVICIO: {self.nombre_entidad} | Tipo: Asesoría Especializada | Área: {self._area} | Nivel: {self._nivel_experto}"

    def validar_registro(self):
        if not self.nombre_entidad or self.costo_base <= 0 or not self._area or self._nivel_experto not in self.MULTIPLICADORES:
            raise ValueError("Datos de la asesoría inválidos.")

    def validar_parametros(self, **kwargs):
        duracion = kwargs.get("duracion")
        if duracion is None or duracion < 0.5:
            raise ValueError("La duración mínima para una asesoría es 0.5 horas.")
        return True