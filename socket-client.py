import socket
from pynput import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 65432
host_ip = '192.168.0.106'

# connecting to the server
s.connect((host_ip, port))

print("connected to pi on port == ", host_ip)


def handle_click(key):
    if key == keyboard.Key.up:
        s.send(b'forward')
    if key == keyboard.Key.down:
        s.send(b'backward')
    if key == keyboard.Key.left:
        s.send(b'left')
    if key == keyboard.Key.right:
        s.send(b'right')
    if key == '+':
        s.send(b'speed up')
    if key == '-':
        s.send(b'speed down')
    if key == 'a':
        s.send(b'cam right')
    if key == 'd':
        s.send(b'cam left')
    if key == 's':
        s.send(b'cam down')
    if key == 'w':
        s.send(b'cam up')


def on_press(key):
    try:
        handle_click(key.char)
    except AttributeError:
        handle_click(key)


def on_release(key):
    s.send(b'stop')
    if key == keyboard.Key.esc:
        return False


while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
