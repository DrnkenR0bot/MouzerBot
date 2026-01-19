import board
import digitalio
from motor_dr import Motor

SLP = digitalio.DigitalInOut(board.D6)
SLP.switch_to_output()
# Enable DRV8833
SLP.value = True



