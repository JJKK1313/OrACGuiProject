import RPi.GPIO as GPIO
import math
import os
from datetime import datetime
from time import sleep

# This is for revision 1 of the Raspberry Pi, Model B
# This pin is also referred to as GPIO23
INPUT_WIRE = 4
REDLED_WIRE = 21
GREENLED_WIRE = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_WIRE, GPIO.IN)
GPIO.setup(REDLED_WIRE, GPIO.OUT)
GPIO.setup(GREENLED_WIRE, GPIO.OUT)

while True:
    value = 1
    # Loop until we read a 0
    while value:
        GPIO.output(GREENLED_WIRE, GPIO.HIGH)
        value = GPIO.input(INPUT_WIRE)

    GPIO.output(GREENLED_WIRE, GPIO.LOW)
    GPIO.output(REDLED_WIRE, GPIO.HIGH)
    # Grab the start time of the command
    startTime = datetime.now()

    # Used to buffer the command pulses
    # command = []
    command = ""

    # The end of the "command" happens when we read more than
    # a certain number of 1s (1 is off for my IR receiver)
    numOnes = 0

    # Used to keep track of transitions from 1 to 0
    previousVal = 0

    while True:

        if value != previousVal:
            # The value has changed, so calculate the length of this run
            now = datetime.now()
            pulseLength = now - startTime
            startTime = now

            # command.append((previousVal, pulseLength.microseconds))
            command += str(pulseLength.microseconds) + ","
        if value:
            numOnes = numOnes + 1
        else:
            numOnes = 0

        # 10000 is arbitrary, adjust as necessary
        if numOnes > 10000:
            break

        previousVal = value
        value = GPIO.input(INPUT_WIRE)

    GPIO.output(REDLED_WIRE, GPIO.LOW)

    print("----------Start----------")
    # for (val, pulse) in command:
    # print (val, pulse)
    print(command)
    print("/n")
    print(command[:len(command) - 1])
    print("-----------End-----------\n")

    print("Size of array is: ")
    print(str(len(command)))
