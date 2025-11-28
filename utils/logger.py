import logging
import os
import sys

class LoggerManager:
    @staticmethod
    def setup_logger():
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger("DigiApp")
        logger.setLevel(logging.INFO)
        
        if logger.hasHandlers():
            logger.handlers.clear()

        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_formatter = logging.Formatter('%(message)s') 

        file_handler = logging.FileHandler(f"{log_dir}/automacao.log", mode='w', encoding='utf-8')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        return logger