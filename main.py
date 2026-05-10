# Importamos tus módulos para que el programa sepa usarlos
from gestion_clientes import Cliente
from proceso_reservas import Reserva

# Importamos los servicios especializados
from servicios_especializados import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

# Importamos el logger para registrar eventos y errores
from logger import registrar_evento, registrar_error, registrar_advertencia

# Intentamos importar el servicio del compañero (si ya corrigió los errores)
try:
    from servicio import Servicio
except:
    # Si aún no lo corrige, creamos una clase temporal para que tus pruebas funcionen
    class Servicio:
        def __init__(self, nombre): self.nombre = nombre

def simulacion_fj():
    print("========== SOFTWARE FJ: SISTEMA DE GESTIÓN ==========")
    
    # PRUEBA 1: Crear un cliente correcto
    try:
        usuario1 = Cliente("Katerin Navas", "12345", "katerin@ejemplo.com")
        print(f"Carga exitosa: {usuario1.mostrar_detalles()}")
    except Exception as e:
        print(f"Fallo en prueba 1: {e}")

    # PRUEBA 2: Forzar error de validación (dejar ID vacío)
    try:
        print("\nProbando validación robusta (ID vacío)...")
        usuario_error = Cliente("Diego", "", "diego@ejemplo.com")
    except ValueError as e:
        print(f"Éxito: El sistema bloqueó el registro vacío: {e}")

    # PRUEBA 3: Realizar una reserva
    try:
        print("\nProcesando reserva de servicio...")
        mi_servicio = Servicio("Mantenimiento de Software")
        reserva1 = Reserva(usuario1, mi_servicio, 4)
        reserva1.procesar_confirmacion()
    except Exception as e:
        print(f"Error al procesar reserva: {e}")

    # PRUEBA 4: Crear una sala válida
    try:
        print("\nCreando servicio de sala...")
        sala = ReservaSala("Sala Júpiter", 50000, 20)
        sala.validar_registro()
        print(sala.describir_servicio())
        registrar_evento(f"Servicio creado: {sala.mostrar_detalles()}")
    except Exception as e:
        registrar_error(e, "Crear ReservaSala")
        print(f"Error al crear sala: {e}")

    # PRUEBA 5: Crear una sala con datos inválidos
    try:
        print("\nProbando sala con capacidad inválida...")
        sala_error = ReservaSala("Sala Error", 50000, -5)
        sala_error.validar_registro()
    except ValueError as e:
        registrar_error(e, "Crear ReservaSala inválida")
        print(f"Éxito: El sistema bloqueó la sala inválida: {e}")

    # PRUEBA 6: Crear un equipo válido
    try:
        print("\nCreando servicio de alquiler de equipo...")
        equipo = AlquilerEquipo("Laptop Dell", 30000, "Laptop", 5)
        equipo.validar_registro()
        print(equipo.describir_servicio())
        registrar_evento(f"Servicio creado: {equipo.mostrar_detalles()}")
    except Exception as e:
        registrar_error(e, "Crear AlquilerEquipo")
        print(f"Error al crear equipo: {e}")

    # PRUEBA 7: Crear una asesoría válida
    try:
        print("\nCreando servicio de asesoría especializada...")
        asesoria = AsesoriaEspecializada("Consultoría IA", 80000, "Inteligencia Artificial", "senior")
        asesoria.validar_registro()
        print(asesoria.describir_servicio())
        registrar_evento(f"Servicio creado: {asesoria.mostrar_detalles()}")
    except Exception as e:
        registrar_error(e, "Crear AsesoriaEspecializada")
        print(f"Error al crear asesoría: {e}")

    # PRUEBA 8: Crear asesoría con nivel inválido
    try:
        print("\nProbando asesoría con nivel inválido...")
        asesoria_error = AsesoriaEspecializada("Consultoría Error", 80000, "Física", "dios")
        asesoria_error.validar_registro()
    except ValueError as e:
        registrar_error(e, "Crear AsesoriaEspecializada inválida")
        print(f"Éxito: El sistema bloqueó la asesoría inválida: {e}")

    # PRUEBA 9: Realizar una reserva con duración inválida
    try:
        print("\nProcesando reserva con duración inválida...")
        reserva2 = Reserva(usuario1, equipo, -2)
        reserva2.procesar_confirmacion()
    except ValueError as e:
        registrar_error(e, "Reserva con duración inválida")
        print(f"Éxito: El sistema bloqueó la reserva inválida: {e}")

    # PRUEBA 10: Calcular costo completo con descuento e impuesto
    try:
        print("\nCalculando costo completo de asesoría...")
        desglose = asesoria.calcular_costo_completo(2, tasa_impuesto=0.19, descuento=0.10)
        for clave, valor in desglose.items():
            print(f"  {clave}: {valor:,.0f}" if isinstance(valor, float) else f"  {clave}: {valor}")
        registrar_evento(f"Costo completo calculado: {desglose['servicio']} | Total: ${desglose['total']:,.0f}")
    except Exception as e:
        registrar_error(e, "Calcular costo completo")
        print(f"Error al calcular costo: {e}")

    print("\n================ SIMULACIÓN FINALIZADA ================")

if __name__ == "__main__":
    simulacion_fj()