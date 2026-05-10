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