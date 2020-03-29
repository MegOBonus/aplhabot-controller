from components import Motor
from pynput import keyboard

motor = Motor()
speed = 50


def handle_click(key):
    print(key)
    if key == 'w' or key == keyboard.Key.up:
        print('forward')
        motor.forward()
    if key == 's' or key == keyboard.Key.down:
        print('backward')
        motor.backward()
    if key == 'a' or key == keyboard.Key.left:
        print('left')
        motor.left()
    if key == 'd' or key == keyboard.Key.right:
        print('right')
        motor.right()
    if key == '+':
        print('speed up')
        motor.speed_up()
    if key == '-':
        print('speed down')
        motor.speed_down()


def on_press(key):
    try:
        # print('alphanumeric key {0} pressed\n'.format(
        #     key.char))
        handle_click(key.char)
    except AttributeError:
        # print('special key {0} pressed\n'.format(
        #     key))
        handle_click(key)


def on_release(key):
    motor.stop()

    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
