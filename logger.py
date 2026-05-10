# Importar módulos necesarios
import logging
import os

# Crear directorio de logs si no existe
os.makedirs("logs", exist_ok=True)
 
# Configurar logging básico
logging.basicConfig(
    filename="logs/softwarefj.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
 
# Obtener logger para SoftwareFJ
logger = logging.getLogger("SoftwareFJ")

# Función para registrar eventos
def registrar_evento(mensaje):
    logger.info(mensaje)
 
# Función para registrar errores
def registrar_error(excepcion, contexto=""):
    if contexto:
        logger.error(f"[{contexto}] {type(excepcion).__name__}: {excepcion}")
    else:
        logger.error(f"{type(excepcion).__name__}: {excepcion}")
 
# Función para registrar advertencias
def registrar_advertencia(mensaje):
    logger.warning(mensaje)