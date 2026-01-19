"""
DrnkenR0bot DC motor library for 2 motor locomotion.
"""
import pwmio

class Motor:
    def __init__(self, pin1, pin2, frequency=2000):
        self.IN1 = pwmio.PWMOut(pin1, frequency=frequency)
        self.IN2 = pwmio.PWMOut(pin2, frequency=frequency)
        self.max_duty_cycle = 65535
        self.min_duty_cycle = 0

    def stop(self):
        self.IN1.duty_cycle = 0
        self.IN2.duty_cycle = 0

    def forward(self, speed: float = 1.0):
        self.IN1.duty_cycle = int(self.max_duty_cycle*speed)
        self.IN2.duty_cycle = 0 

    def backward(self, speed: float = 1.0):
        self.IN1.duty_cycle = 0
        self.IN2.duty_cycle = int(self.max_duty_cycle*speed)

class Loco:
    def __init__(self, left_motor: Motor, right_motor: Motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def forward(self, speed: float = 1.0):
        self.left_motor.forward(speed=speed)
        self.right_motor.forward(speed=speed)

    def backward(self, speed: float = 1.0):
        self.left_motor.backward(speed=speed)
        self.right_motor.backward(speed=speed)

    def right_spin(self, speed: float = 0.25):
        self.left_motor.forward(speed=speed)
        self.right_motor.backward(speed=speed)

    def left_spin(self, speed: float = 0.25):
        self.left_motor.backward(speed=speed)
        self.right_motor.forward(speed=speed)

