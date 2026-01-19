"""
DrnkenR0bot DC motor library for 2 motor locomotion.
"""
import pwmio


class Motor:
    def __init__(self, pin1, pin2, frequency=2000):
        self.IN1 = pwmio.PWMOut(pin1, frequency=frequency)
        self.IN2 = pwmio.PWMOut(pin2, frequency=frequency)
        self.max_duty_cycle = 65536
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

