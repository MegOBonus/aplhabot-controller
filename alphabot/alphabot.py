from .components import Motor, Servo


class Alphabot(object):
    def __init__(self):
        horizontal_servo_pin = 22
        vertical_servo_pin = 27
        self.motor = Motor()
        self.vertical_servo = Servo(vertical_servo_pin)
        self.horizontal_servo = Servo(horizontal_servo_pin)

    def go_forward(self):
        self.motor.forward()

    def stop_motor(self):
        self.motor.stop()

    def go_backward(self):
        self.motor.backward()

    def turn_left(self):
        self.motor.right()

    def turn_right(self):
        self.motor.right()

    def set_speed(self, value):
        self.motor.set_speed(value)

    def motor_speed_up(self):
        self.motor.speed_up()

    def motor_speed_down(self):
        self.motor.speed_down()

    def turn_camera_up(self):
        self.vertical_servo.left()

    def turn_camera_down(self):
        self.vertical_servo.right()

    def turn_camera_left(self):
        self.horizontal_servo.left()

    def turn_camera_right(self):
        self.horizontal_servo.right()

