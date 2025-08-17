


import logging
import os 



def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # ✅ If logger already has handlers, return it directly
    if logger.handlers:
        return logger

    # Formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    

    
    logger.addHandler(console_handler)
    

    return logger



logger = get_logger(__name__)

