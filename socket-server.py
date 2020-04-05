import sys
import socket
import selectors
import types
from components import Motor, Servo

motor = Motor()
speed = 50
sel = selectors.DefaultSelector()
s1 = Servo(27)
s2 = Servo(22)


def handle_msg(key):
    print(key)
    if key == b'forward':
        motor.forward()
    if key == b'backward':
        motor.backward()
    if key == b'left':
        motor.left()
    if key == b'right':
        motor.right()
    if key == b'speed up':
        motor.speed_up()
    if key == b'speed down':
        motor.speed_down()
    if key == b'stop':
        motor.stop()
    if key == b'cam up':
        s1.left()
    if key == b'cam down':
        s1.right()
    if key == b'cam left':
        s2.left()
    if key == b'cam right':
        s2.right()


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
