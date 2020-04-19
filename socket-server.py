import socketserver
import logging
from alphabot import Alphabot

logger = logging.getLogger('alphabot-logger')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, host_port_tuple, streamhandler, alphabot):
        super().__init__(host_port_tuple, streamhandler)
        self.alphabot = alphabot


class Handler(socketserver.StreamRequestHandler):
    def __init__(self, request, client_address, server):
        self.data = b''
        super().__init__(request, client_address, server)

    def handle_command(self, key):
        if key == b'forward':
            self.server.alphabot.go_forward()
        if key == b'backward':
            self.server.alphabot.go_backward()
        if key == b'left':
            self.server.alphabot.turn_left()
        if key == b'right':
            self.server.alphabot.turn_right()
        if key == b'speed up':
            self.server.alphabot.motor_speed_up()
        if key == b'speed down':
            self.server.alphabot.motor_speed_down()
        if key == b'stop':
            self.server.alphabot.stop_motor()
        if key == b'cam up':
            self.server.alphabot.turn_camera_up()
        if key == b'cam down':
            self.server.alphabot.turn_camera_down()
        if key == b'cam left':
            self.server.alphabot.turn_camera_left()
        if key == b'cam right':
            self.server.alphabot.turn_camera_right()

    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.handle_command(self.data)
        logger.debug('Message received {}'.format(str(self.data)))


if __name__ == "__main__":
    HOST, PORT = '192.168.0.101', 65432
    logger.debug('Server started on {}:{}'.format(HOST, PORT))

    bot = Alphabot()
    server = Server((HOST, PORT), Handler, bot)
    server.serve_forever()
