import RPi.GPIO as GPIO
import time


class Servo(object):

    def __init__(self, pin ):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.angle_step = 10  # degrees
        self.servo_angle = 90
        self.servo.start(0)
        self.change_angle(self.servo_angle)

    def change_angle(self, angle):
        self.servo.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(0)
        print(angle)

    def right(self):
        if self.servo_angle + self.angle_step < 180:
            self.servo_angle += self.angle_step
            self.change_angle(self.servo_angle)

    def left(self):
        if self.servo_angle - self.angle_step > 0:
            self.servo_angle -= self.angle_step
            self.change_angle(self.servo_angle)


