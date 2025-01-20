from multiprocessing import Process, Array
import os # Gives Python access to Linux commands
import time # Proves time related commands
import RPi.GPIO as GPIO # Gives Python access to the GPIO pins
import pigpio

#GPIO Initial setup
GPIO.setmode(GPIO.BCM) # Set the GPIO pin naming mode
GPIO.setwarnings(False) # Suppress warnings
pi = pigpio.pi()

#Variable setup
Button1 = 12
Button2 = 13
Button3 = 26
Button4 = 25
Button5 = 22
Relay1 = 16
Relay2 = 6
Switch1 = 5
b1led = 20
b2led = 19
b3led = 7
b4led = 3
b5led = 2
Light_Sensor = 27
EyeL = 21
EyeR = 18
disp = tm1637.TM1637(23, 24)
pir = 17
redm = 11
bluem = 9
greenm = 10
whitem = 8

#GPIO Resistor and pin setup
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Relay1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Relay2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pir, GPIO.IN)
GPIO.setup(Light-Sensor, GPIO.IN)
GPIO.setup(b1led, GPIO.OUT)
GPIO.setup(b2led, GPIO.OUT)
GPIO.setup(b3led, GPIO.OUT)
GPIO.setup(b4led, GPIO.OUT)
GPIO.setup(b5led, GPIO.OUT)
GPIO.setup(redm, GPIO.OUT)
GPIO.setup(bluem, GPIO.OUT)
GPIO.setup(greenm, GPIO.OUT)
GPIO.setup(whitem, GPIO.OUT)
GPIO.setup(EyeL, GPIO.OUT)
GPIO.setup(EyeR, GPIO.OUT)

#Code:

def button-sense()
	while True:
		if GPIO.input(Switch1) == GPIO.LOW:	
			if GPIO.input(Button1) == GPIO.HIGH:
				pass
			if GPIO.input(Button2) == GPIO.HIGH:
				pass
			if GPIO.input(Button3) == GPIO.HIGH:
				pass
			if GPIO.input(Button4) == GPIO.HIGH:
				pass
			if GPIO.input(Button5) == GPIO.HIGH:
				pass
			if GPIO.input(Relay1) == GPIO.HIGH:
				pass
			if GPIO.input(Relay2) == GPIO.HIGH:
				pass
		elif GPIO.input(Switch1) == GPIO.HIGH:
			if GPIO.input(Button1) == GPIO.HIGH:
				pass
			if GPIO.input(Button2) == GPIO.HIGH:
				pass
			if GPIO.input(Button3) == GPIO.HIGH:
				pass
			if GPIO.input(Button4) == GPIO.HIGH:
				pass
			if GPIO.input(Button5) == GPIO.HIGH:
				pass
			if GPIO.input(Relay1) == GPIO.HIGH:
				pass
			if GPIO.input(Relay2) == GPIO.HIGH:
				pass



















if __name__ == '__main__':