import socketserver
from .alphabot import Alphabot


class CommandTCPHandler(socketserver.StreamRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.alphabot = Alphabot()
        self.data = b''

    def handle_command(self, key):
        if key == b'forward':
            self.alphabot.go_forward()
        if key == b'backward':
            self.alphabot.go_backward()
        if key == b'left':
            self.alphabot.turn_left()
        if key == b'right':
            self.alphabot.turn_right()
        if key == b'speed up':
            self.alphabot.motor_speed_up()
        if key == b'speed down':
            self.alphabot.motor_speed_down()
        if key == b'stop':
            self.alphabot.stop_motor()
        if key == b'cam up':
            self.alphabot.turn_camera_up()
        if key == b'cam down':
            self.alphabot.turn_camera_down()
        if key == b'cam left':
            self.alphabot.turn_camera_left()
        if key == b'cam right':
            self.alphabot.turn_camera_right()

    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.handle_command(self.data)
        print(self.data)


if __name__ == "__main__":
    HOST, PORT = '192.168.0.106', 65432

    with socketserver.TCPServer((HOST, PORT), CommandTCPHandler) as server:
        server.serve_forever()
