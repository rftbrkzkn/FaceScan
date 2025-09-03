import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

class Logger:
    @staticmethod
    def log(message, level="info"):
        getattr(logging, level)(message)
