import logging

logger = logging.getLogger(__name__)


def print_hello():
    print("hello")
    logger.info("Cro job was Called")