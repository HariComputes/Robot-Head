import time
import pigpio
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Set the GPIO pin naming mode
GPIO.setwarnings(False) # Suppress warnings
pi = pigpio.pi()


b1led = 20
b2led = 19
b3led = 7
b4led = 3
b5led = 2
Light_Sensor = 27
EyeL = 21
EyeR = 18
pir = 17
redm = 11
bluem = 9
greenm = 10
whitem = 8


def mouthlight(mode):
	if mode == 0:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 1:
		pi.set_PWM_dutycycle(redm, 255)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 2:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 3:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 4:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 255)
	elif mode == 5:
		pi.set_PWM_dutycycle(redm, 255)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 6:
		pi.set_PWM_dutycycle(redm, 255)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 7:
		pi.set_PWM_dutycycle(redm, 255)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 255)
	elif mode == 8:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 9:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 0)
		pi.set_PWM_dutycycle(whitem, 255)
	elif mode == 10:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 0)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 255)
	elif mode == 11:
		pi.set_PWM_dutycycle(redm, 255)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 0)
	elif mode == 12:
		pi.set_PWM_dutycycle(redm, 255)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 255)
	elif mode == 13:
		pi.set_PWM_dutycycle(redm, 0)
		pi.set_PWM_dutycycle(bluem, 255)
		pi.set_PWM_dutycycle(greenm, 255)
		pi.set_PWM_dutycycle(whitem, 255)








				