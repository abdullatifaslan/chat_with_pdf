import logging
from pathlib import Path
import os

LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
Path(os.path.dirname(LOG_FILE)).mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("app_logger")
