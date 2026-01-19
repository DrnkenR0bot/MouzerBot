import board
import digitalio
from time import sleep
from motor_dr import Motor, Loco

# Initialize left and right motors
left_motor = Motor(board.D2, board.D3)
right_motor = Motor(board.D4, board.D5)

# Initialize Loco(motion) control
loco = Loco(left_motor, right_motor)

# Enable DRV8833 motor driver
loco.stop() # bring pins to stop setting before activating driver
SLP = digitalio.DigitalInOut(board.D6)
SLP.switch_to_output()
SLP.value = True

# As a test, drive straight, reverse, turn, turn, and stop
def drive_test(drive_speed: float, turn_speed: float):
    sleep(5)

    loco.forward(speed=drive_speed)
    sleep(1)
    loco.stop()
    sleep(1)

    loco.backward(speed=drive_speed)
    sleep(1)
    loco.stop()
    sleep(1)

    loco.right_spin(speed=turn_speed)
    sleep(1)
    loco.stop()
    sleep(1)

    loco.left_spin(speed=turn_speed)
    sleep(1)
    loco.stop()
    sleep(1)
    # we should be back where we started, depending on motor control accuracy

if __name__ == "__main__":
    drive_test(0.5, 0.25)
