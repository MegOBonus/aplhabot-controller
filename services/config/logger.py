from os import environ
import logging

logger = logging.getLogger('alphabot-logger')
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.DEBUG if environ.get("ENV") == "dev" else logging.WARNING)
