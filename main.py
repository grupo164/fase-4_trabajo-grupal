# Importamos tus módulos para que el programa sepa usarlos
from gestion_clientes import Cliente
from proceso_reservas import Reserva

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
        reserva1 = Reserva(usuario1, mi_servicio, 4) # 4 horas
        reserva1.procesar_confirmacion()
    except Exception as e:
        print(f"Error al procesar reserva: {e}")

    print("\n================ SIMULACIÓN FINALIZADA ================")

if __name__ == "__main__":
    simulacion_fj()
