import board
import digitalio
import adafruit_hcsr04
from time import sleep
from motor_dr import Motor, Loco

# Initialize sonar
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A3, echo_pin=board.A2)

def distance(cm2xscale=1e-2):
    """
    Return sonar distance to object.
    
    :param cm2xscale: Use to scale from native cm to any units. Default is meters (1e-2).
    """
    return sonar.distance*cm2xscale

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


def drive_test(drive_speed: float, turn_speed: float):
    print("Initiating drive test...")
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

def distance_test():
    print("Initiating sonar test, KeyboardInterrupt to stop...")
    sleep(3)
    while True:
        try:
            print(distance())
            sleep(0.5)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    drive_test(0.5, 0.25)
    distance_test()
