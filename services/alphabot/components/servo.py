import RPi.GPIO as GPIO
import time
import logging


class Servo(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.angle_step = 20  # degrees
        self.servo_angle = 90
        self.servo.start(0)
        self.logger = logging.getLogger('alphabot-logger')
        self.logger.debug('Servo on {} pin ready'.format(pin))
        self.change_angle(self.servo_angle)

    def change_angle(self, angle):
        self.servo.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.1)
        self.servo.ChangeDutyCycle(0)
        self.logger.debug('Servo on {} pin current angle {}'.format(self.pin, angle))

    def right(self):
        if self.servo_angle + self.angle_step < 180:
            self.servo_angle += self.angle_step
            self.change_angle(self.servo_angle)

    def left(self):
        if self.servo_angle - self.angle_step > 0:
            self.servo_angle -= self.angle_step
            self.change_angle(self.servo_angle)


