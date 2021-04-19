import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO numbers instead of board numbers

RELAYS_1_GPIO = 17
GPIO.setup(RELAYS_1_GPIO, GPIO.OUT) # GPIO Assign mode

while(True):
    time.sleep(1)
    print("OFF")
    GPIO.output(RELAYS_1_GPIO, GPIO.LOW) # OFF
    time.sleep(1)
    print("ON")
    GPIO.output(RELAYS_1_GPIO, GPIO.HIGH) # ON
