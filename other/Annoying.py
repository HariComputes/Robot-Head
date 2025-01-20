import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
import pyttsx3
import pigpio
pi=pigpio.pi()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#CLK -> GPIO23 (Pin 16)
#Di0 -> GPIO24 (Pin 18)

engine = pyttsx3.init()

ptc = 27
ledpin = 11
clock = 1
disp = tm1637.TM1637(23, 24)
#Display.Clear()
#Display.SetBrightnes(1)
GPIO.setup(ptc, GPIO.IN)
pinpir = 17
#print("PIR Module Test (CTRL-C to exit)")
# Set pin as input
GPIO.setup(pinpir, GPIO.IN)
# Variables to hold the current and last states
currentstate = 0
previousstate = 0
senstrig = 0

volume = voiceEngine.getProperty('volume')
print(volume)

def clocksense():
	global clock
	global disp
	global pinpir
	global currentstate
	global previousstate
	global engine
	global ptc
	global senstrig

	try:
		#print("Waiting for PIR to settle ...")
		# Loop until PIR output is 0
		while GPIO.input(pinpir) == 1:
			currentstate = 0

		while clock == 1:
			now = datetime.datetime.now()
			hours = now.strftime('%I')
			hour = int(hours)
	#		hour = now.hour
			minute = now.minute
			second = now.second
			currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]
			disp.set_values(currenttime)
			disp.set_doublepoint(second % 2)
			time.sleep(1)
			# Read PIR state
			currentstate = GPIO.input(pinpir)
			count = 0
  
			#Output on the pin for 
			GPIO.setup(ptc, GPIO.OUT)
			GPIO.output(ptc, GPIO.LOW)
			time.sleep(0.1)

			#Change the pin back to input
			GPIO.setup(ptc, GPIO.IN)
  
			#Count until the pin goes high
			while (GPIO.input(ptc) == GPIO.LOW):
				count += 1
			if count >= 10000:
				if senstrig != 2:
					senstrig = senstrig + 1
				if senstrig == 2:
					pi.set_PWM_dutycycle(ledpin, 10)
			else:
				if senstrig > 0:
					senstrig = senstrig - 1
				elif senstrig == 0:
					pi.set_PWM_dutycycle(ledpin, 0)

		
			# If the PIR is triggered
			if currentstate == 1 and previousstate == 0:
				#print(" Motion detected!")
				smile = ["happy1", "happy2", "happy2", "happy3"]
				disp.set_doublepoint(0)
				disp.set_values(smile)
				engine.say("Hello")
				engine.runAndWait()
				time.sleep(1)

				# Record previous state
				previousstate = 1
				
	
			# If the PIR has returned to ready state
			elif currentstate == 0 and previousstate == 1:
				#print(" Ready")
				previousstate = 0
				
	
			# Wait for 10 milliseconds
			time.sleep(0.01)
	except KeyboardInterrupt:
		print(" Quit")
		# Reset GPIO settings
		GPIO.cleanup()

clocksense()

def greet():
	global clock
	global disp
	global pinpir
	global currentstate
	global previousstate
	global engine
	engine.say("Hello")
	smile = [smi1, smi2, smi2, smi3]
	disp.set_doublepoint(0)
	disp.set_values(smile)
	engine.runAndWait()
	clocksense()
	



#pinpir = 17
#print("PIR Module Test (CTRL-C to exit)")
# Set pin as input
#GPIO.setup(pinpir, GPIO.IN)
# Variables to hold the current and last states
#currentstate = 0
#previousstate = 0
#try:
	#print("Waiting for PIR to settle ...")
	# Loop until PIR output is 0
#	while GPIO.input(pinpir) == 1:
#		currentstate = 0

	#print(" Ready")
	# Loop until users quits with CTRL-C
#	while True:
		# Read PIR state
#		currentstate = GPIO.input(pinpir)
		
		# If the PIR is triggered
#		if currentstate == 1 and previousstate == 0:
			#print(" Motion detected!")
#			greet()
			# Record previous state
#			previousstate = 1
	
		# If the PIR has returned to ready state
#		elif currentstate == 0 and previousstate == 1:
#			#print(" Ready")
#			previousstate = 0
#	
#		# Wait for 10 milliseconds
#		time.sleep(0.01)

