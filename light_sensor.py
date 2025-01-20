#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"

#GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 13

def rc_time (pin_to_circuit):
    count = 0
    light = 0
    senstrig = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
	if count >= 10000:
		if senstrig != 2:
			senstrig = senstrig + 1
		if senstrig == 2:
			light = 0
	else:
		if senstrig > 0:
			senstrig = senstrig - 1
		elif senstrig == 0:
			light = 1

    return light

