import json

socket_server = json.load(open('config/config.json'))["socket-server"]
camera_stream = json.load(open('config/config.json'))["camera-stream"]
commads = json.load(open('config/commands.json'))

from .logger import logger
