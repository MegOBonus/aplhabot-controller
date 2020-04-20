import RPi.GPIO as GPIO
import logging


class Motor(object):

    def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26, speed=50, speed_step=10):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb
        self.speed = speed
        self.speed_step = speed_step
        self.min_duty_cycle = 40
        self.max_duty_cycle = 100

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        self.PWMA = GPIO.PWM(self.ENA, 500)
        self.PWMB = GPIO.PWM(self.ENB, 500)
        self.PWMA.start(self.speed)
        self.PWMB.start(self.speed)
        self.logger = logging.getLogger('alphabot-logger')
        self.logger.debug('Motor ready')

    def forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.logger.debug('Forward')

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.logger.debug('Stop')

    def backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.logger.debug('Backward')

    def left(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.logger.debug('Left')

    def right(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.logger.debug('Right')

    def set_speed(self, value):
        self.PWMA.ChangeDutyCycle(value)
        self.PWMB.ChangeDutyCycle(value)
        self.logger.debug('Current speed = {}'.format(value))

    def speed_up(self):
        if self.speed + self.speed_step <= self.max_duty_cycle:
            self.speed += self.speed_step
            self.set_speed(self.speed)

    def speed_down(self):
        if self.speed - self.speed_step >= self.min_duty_cycle:
            self.speed -= self.speed_step
            self.set_speed(self.speed)
