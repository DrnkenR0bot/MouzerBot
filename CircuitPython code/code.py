import board
import digitalio
import adafruit_hcsr04
import random
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

def proximity(proximity_distance = 5.e-2):
    """
    Return True if distance to object < proximity_distance.
    
    :param proximity_distance: Trigger distance from ultrasonic sensor in meters.
    """
    sleep(0.01) # Need a little sleep time between proximity checks for sensor response.
    if distance() < proximity_distance:
        print("PROXIMITY!")
        return True
    else:
        return False

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


def drive_test(drive_speed: float = 1, turn_speed: float = 0.8):
    print("Initiating drive test...")
    sleep(1)

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
    sleep(1)
    while True:
        try:
            print(distance())
            sleep(0.5)
        except KeyboardInterrupt:
            break

def basic_avoidance(speed=0.5, between_readings=0.1, standoff=10.e-2):
    print("Initiating basic avoidance test, KeyboardInterrupt to stop...")
    sleep(1)
    while True:
        try:
            while distance() > standoff:
                loco.forward(speed=speed)
                sleep(between_readings)
            else:
                loco.stop()
                sleep(0.01)
        except KeyboardInterrupt:
            break
    print("Interrupt detected.")

def roam(speed=1, proximity_distance=10.e-2, bump_scale=1.0):
    """
    Roam around via random walk. Avoid obstacles.
    
    :param speed: max speed of motors, <= 1.
    """        
    def bump(speed=0.5):
        """
        Action to perform if proximity detected.

        :param speed: max speed of motors, <= 1.
        """
        turn_speed = speed
        loco.stop()
        loco.backward(speed=speed)
        sleep(3*random.random())
        loco.stop()
        turn_direction = random.getrandbits(1) # 0 = left, 1 = right
        turn_time = 0.5 + 3*random.random()
        if turn_direction == 0:
            loco.left_turn(speed=turn_speed, turn_time=turn_time)
        else:
            loco.right_turn(speed=turn_speed, turn_time=turn_time)

    while True:
        loco.forward(speed=speed)
        if proximity(proximity_distance=proximity_distance):
            bump(speed=bump_scale*speed)


if __name__ == "__main__":
    #basic_avoidance(speed=1)
    roam(speed=0.8, proximity_distance=20.e-2)
