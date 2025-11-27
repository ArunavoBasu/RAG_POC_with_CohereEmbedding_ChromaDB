import logging
import os
from datetime import datetime

### Initializing the logger
def logger_func():
    try: 
            os.makedirs("logs", exist_ok=True)
            log_file_name = datetime.now().strftime("logs/run_%H-%M-%S.log")
            logging.basicConfig(
                filename=log_file_name,
                format="%(asctime)s | %(levelname)s | %(message)s"
            )
            logger = logging.getLogger()
            return logger

    except Exception as LogFileError:
        print (LogFileError)
