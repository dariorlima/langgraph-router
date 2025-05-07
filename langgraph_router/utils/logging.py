import logging
import os

def setup_logger(name: str, log_file=None):
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO if not set
    log_level = getattr(logging, log_level, logging.INFO)  # Ensure valid log level

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        # File Handler (if log_file is provided)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
