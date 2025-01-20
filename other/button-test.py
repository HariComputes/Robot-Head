import os # Gives Python access to Linux commands
import time # Proves time related commands
import RPi.GPIO as GPIO # Gives Python access to the GPIO pins
GPIO.setmode(GPIO.BCM) # Set the GPIO pin naming mode
GPIO.setwarnings(False) # Suppress warnings

Button5 = 22
Button2 = 13
Button3 = 26
Button4 = 25
Button1 = 12
Relay1 = 16
Switch1 = 5
Relay2 = 6

GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Relay1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Relay2, GPIO.IN, pull_up_down=GPIO.PUD_UP)



button1State = GPIO.input(Button1)
button2State = GPIO.input(Button2)
button3State = GPIO.input(Button3)
button4State = GPIO.input(Button4)
button5State = GPIO.input(Button5)
Switch1State = GPIO.input(Switch1)
Relay1State = GPIO.input(Relay1)
Relay2State = GPIO.input(Relay2)

print("Button is 0 when pressed and 1 when not. Relay is 1 when power is present and 0 when not")

print("Button1 state is ", button1State)
print("Button2 state is ", button2State)
print("Button3 state is ", button3State)
print("Button4 state is ", button4State)
print("Button5 state is ", button5State)
print("Switch1 state is ", Switch1State)
print("USB-C state is ", Relay1State)
print("240V state is ", Relay2State)