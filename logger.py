import logging
import os

os.makedirs("logs", exist_ok=True)
 
logging.basicConfig(
    filename="logs/softwarefj.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
 
logger = logging.getLogger("SoftwareFJ")

def registrar_evento(mensaje):
    logger.info(mensaje)
 
def registrar_error(excepcion, contexto=""):
    if contexto:
        logger.error(f"[{contexto}] {type(excepcion).__name__}: {excepcion}")
    else:
        logger.error(f"{type(excepcion).__name__}: {excepcion}")
 
def registrar_advertencia(mensaje):
    logger.warning(mensaje)