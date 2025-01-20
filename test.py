import light_sensor
import RPi.GPIO as GPIO # Gives Python access to the GPIO pins

Button1 = 12

GPIO.setmode(GPIO.BCM) # Set the GPIO pin naming mode
GPIO.setwarnings(False) # Suppress warnings
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:
	if GPIO.input(Button1) == GPIO.LOW:
		print(light_sensor.rc_time(27))