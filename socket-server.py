import socket
import selectors
import types
from .alphabot import Alphabot

sel = selectors.DefaultSelector()
alphabot = Alphabot()


def handle_msg(key):
    print(key)
    if key == b'forward':
        alphabot.go_forward()
    if key == b'backward':
        alphabot.go_backward()
    if key == b'left':
        alphabot.turn_left()
    if key == b'right':
        alphabot.turn_right()
    if key == b'speed up':
        alphabot.motor_speed_up()
    if key == b'speed down':
        alphabot.motor_speed_down()
    if key == b'stop':
        alphabot.stop_motor()
    if key == b'cam up':
        alphabot.turn_camera_up()
    if key == b'cam down':
        alphabot.turn_camera_down()
    if key == b'cam left':
        alphabot.turn_camera_left()
    if key == b'cam right':
        alphabot.turn_camera_right()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            handle_msg(data.outb)
            data.outb = b''


host, port = '192.168.0.106', 65432
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
