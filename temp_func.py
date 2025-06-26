#from multiprocessing import Process, Array
import os # Gives Python access to Linux commands
import time # Proves time related commands
import RPi.GPIO as GPIO # Gives Python access to the GPIO pins
import pigpio
import clock
import light_effects
#import threading
import multiprocessing
import temperature
import tm1637
import rgb_toggle_state
import light_sensor_current

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
ditr = 0
lightstate = 0
#Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
lightsensormode = 0
#clockproc = threading.Thread(target=clock.clock, name="Clock", args=(1,))
#mp = multiprocessing.get_context('spawn')
brightness_check = 0


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
GPIO.setup(Light_Sensor, GPIO.IN)
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


while True:
	if GPIO.input(Switch1) == GPIO.LOW:
		if ditr == 0:
			#p = threading.Thread(target=light_effects.dwr, name="eyes", args=(0.5, 5, 10))
			p = multiprocessing.Process(target=light_effects.dwr, name="eyes", args=(0.5, 5, 10))
			p.start()
			light_effects.pulse(0.0005)
			light_effects.pulse(0.0005)		
			light_effects.ltr(0.0005)
			light_effects.rtl(0.0005)
			light_effects.out_fade(0.0005)
			light_effects.out_fade(0.0005)
			light_effects.buttons_on(255)
			light_effects.eyes_on(10)
			ditr = 1

		clockproc = multiprocessing.Process(target=clock.clock, name="Clock", args=(1,))
		clockproc.start()
		#clock.clock(1)
		#lp = threading.Thread(target=light_sensor_current.rc_time, name="Nightlight", args=(Light_Sensor,))
		sensor_results_queue = multiprocessing.Queue()
		lp = multiprocessing.Process(target=light_sensor_current.rc_time, name="Nightlight", args=(Light_Sensor,sensor_results_queue))
		lp.start()
		#if GPIO.input(pir) == 1:
		#	pi.set_PWM_dutycycle(redm, 55)
		#elif GPIO.input(pir) == 0:
		#	pi.set_PWM_dutycycle(redm, 0)
		if GPIO.input(Button2) == GPIO.LOW:
			if lightstate == 13:
				lightstate = 0
			lightstate = lightstate + 1
			rgb_toggle_state.mouthlight_PWM(lightstate, 255)
		if GPIO.input(Button1) == GPIO.LOW:
			temper = temperature.read_temp()
			dispout = [ int(temper / 10), temper % 10, "deg", "C"]
			clockproc.terminate()
			clock.clock(0)
			disp.set_values(dispout)
			time.sleep(5)
		if GPIO.input(Button3) == GPIO.LOW:
			lightstate = 0
			rgb_toggle_state.mouthlight_PWM(lightstate, 255)
		if GPIO.input(Button4) == GPIO.LOW:
			if lightsensormode == 1:
				lightsensormode = 0
			elif lightsensormode == 0:
				lightsensormode = 1
		results_queue = multiprocessing.Queue()
		light_intensity = sensor_results_queue.get()
		if lightsensormode == 1: 
			if lightstate <= 4:
				if light_intensity > 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 130)
				elif light_intensity > 10000 and light_intensity < 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 30)
				elif light_intensity < 10000 and light_intensity > 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 5)
				elif light_intensity < 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 0)
			elif lightstate > 4 and lightstate < 11:
				if light_intensity > 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 65)
				elif light_intensity > 10000 and light_intensity < 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 15)
				elif light_intensity < 10000 and light_intensity > 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 2)
				elif light_intensity < 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 0)
			elif lightstate == 11 or lightstate == 13:
				if light_intensity > 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 42)
				elif light_intensity > 10000 and light_intensity < 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 10)
				elif light_intensity < 10000 and light_intensity > 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 2)
				elif light_intensity < 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 0)
			elif lightstate == 12:
				if light_intensity > 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 33)
				elif light_intensity > 10000 and light_intensity < 1000000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 8)
				elif light_intensity < 10000 and light_intensity > 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 1)
				elif light_intensity < 5000:
					rgb_toggle_state.mouthlight_PWM(lightstate, 0)



			
				
			
	elif GPIO.input(Switch1) == GPIO.HIGH:
			light_effects.eyes_off()
			light_effects.buttons_off()
			pi.set_PWM_dutycycle(redm, 0)
			clockproc.terminate()
			clock.clock(0)
			ditr = 0








		