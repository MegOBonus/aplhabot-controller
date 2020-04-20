import socketserver
from alphabot import Alphabot
from config import socket_server, logger, commads


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, host_port_tuple, streamhandler, alphabot):
        super().__init__(host_port_tuple, streamhandler)
        self.alphabot = alphabot


class Handler(socketserver.StreamRequestHandler):
    def __init__(self, request, client_address, server):
        self.data = ''
        super().__init__(request, client_address, server)

    def handle_command(self, key):
        if key == commads["motor"]["forward"]:
            self.server.alphabot.go_forward()
        if key == commads["motor"]["backward"]:
            self.server.alphabot.go_backward()
        if key == commads["motor"]["left"]:
            self.server.alphabot.turn_left()
        if key == commads["motor"]["right"]:
            self.server.alphabot.turn_right()
        if key == commads["motor"]["speed"]["up"]:
            self.server.alphabot.motor_speed_up()
        if key == commads["motor"]["speed"]["down"]:
            self.server.alphabot.motor_speed_down()
        if key == commads["motor"]["stop"]:
            self.server.alphabot.stop_motor()
        if key == commads["camera"]["up"]:
            self.server.alphabot.turn_camera_up()
        if key == commads["camera"]["down"]:
            self.server.alphabot.turn_camera_down()
        if key == commads["camera"]["left"]:
            self.server.alphabot.turn_camera_left()
        if key == commads["camera"]["right"]:
            self.server.alphabot.turn_camera_right()

    def handle(self):
        self.data = self.request.recv(1024).strip().decode('utf-8')
        logger.debug('Message received {}'.format(self.data))
        self.handle_command(self.data)


if __name__ == "__main__":
    bot = Alphabot()

    host, port = socket_server["host"], socket_server["port"]
    server = Server((host, port), Handler, bot)
    logger.debug('Server started on {}:{}'.format(host, port))
    server.serve_forever()
