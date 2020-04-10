import socket
from pynput import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 65432
host_ip = '192.168.0.106'


def send_msg(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host_ip, port))
        sock.sendall(msg)


def handle_click(key):
    if key == keyboard.Key.up:
        send_msg(b'forward')
    if key == keyboard.Key.down:
        send_msg(b'backward')
    if key == keyboard.Key.left:
        send_msg(b'left')
    if key == keyboard.Key.right:
        send_msg(b'right')
    if key == '+':
        send_msg(b'speed up')
    if key == '-':
        send_msg(b'speed down')
    if key == 'a':
        send_msg(b'cam right')
    if key == 'd':
        send_msg(b'cam left')
    if key == 's':
        send_msg(b'cam down')
    if key == 'w':
        send_msg(b'cam up')


def on_press(key):
    try:
        handle_click(key.char)
    except AttributeError:
        handle_click(key)


def on_release(key):
    send_msg(b'stop')
    if key == keyboard.Key.esc:
        return False


while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
