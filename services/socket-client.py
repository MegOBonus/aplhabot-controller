import socket
from pynput import keyboard
from config import socket_server, commads

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = socket_server["port"]
host_ip = socket_server["host"]


def send_msg(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host_ip, port))
        sock.sendall(msg)


def handle_click(key):
    if key == keyboard.Key.up:
        send_msg(bytes(commads["motor"]["forward"]))
    if key == keyboard.Key.down:
        send_msg(bytes(commads["motor"]["backward"]))
    if key == keyboard.Key.left:
        send_msg(bytes(commads["motor"]["left"]))
    if key == keyboard.Key.right:
        send_msg(bytes(commads["motor"]["right"]))
    if key == '+':
        send_msg(bytes(commads["motor"]["speed"]["up"]))
    if key == '-':
        send_msg(bytes(commads["motor"]["speed"]["down"]))
    if key == 'a':
        send_msg(bytes(commads["camera"]["right"]))
    if key == 'd':
        send_msg(bytes(commads["camera"]["left"]))
    if key == 's':
        send_msg(bytes(commads["camera"]["down"]))
    if key == 'w':
        send_msg(bytes(commads["camera"]["up"]))


def on_press(key):
    try:
        handle_click(key.char)
    except AttributeError:
        handle_click(key)


def on_release(key):
    send_msg(bytes(commads["motor"]["stop"]))
    if key == keyboard.Key.esc:
        return False


while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
