import logging
import os
from datetime import datetime

def logger_func():
    os.makedirs("logs", exist_ok=True)

    log_file_name = datetime.now().strftime("run_%Y-%m-%d_%H-%M-%S.log")
    log_file_path = os.path.join("logs", log_file_name)

    logger = logging.getLogger("RAG_LOGGER")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:

        # File Handler
        fh = logging.FileHandler(log_file_path, encoding="utf-8")
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        fh.setFormatter(formatter)

        logger.addHandler(fh)

    return logger
