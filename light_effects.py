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


def in_fade(fade_gap):
	st0 = 0
	st1 = 0
	aa = 0
	ab = 255
	ba = 0
	bb = 255
	ca = 0
	cb = 255
	#fade_gap = 0.003

	while aa != 255:
		pi.set_PWM_dutycycle(b1led, aa)
		pi.set_PWM_dutycycle(b5led, aa)
		aa = aa + 1
		time.sleep(fade_gap)
		if aa == 127:
			st0 = 1
		if st0 == 1:
			pi.set_PWM_dutycycle(b2led, ba)
			pi.set_PWM_dutycycle(b4led, ba)
			ba = ba + 1
	while ab != 0:
		pi.set_PWM_dutycycle(b1led, ab)
		pi.set_PWM_dutycycle(b5led, ab)
		ab = ab - 1
		pi.set_PWM_dutycycle(b3led, ca)
		ca = ca + 1
		time.sleep(fade_gap)
		if st0 == 1:
			pi.set_PWM_dutycycle(b2led, ba)
			pi.set_PWM_dutycycle(b4led, ba)
			ba = ba + 1
			if ba == 255:
				st0 = 0
		elif st0 == 0:
			pi.set_PWM_dutycycle(b2led, bb)
			pi.set_PWM_dutycycle(b4led, bb)
			bb = bb - 1

			
	while bb != 0:
		pi.set_PWM_dutycycle(b2led, bb)
		pi.set_PWM_dutycycle(b4led, bb)
		bb = bb - 1
		time.sleep(fade_gap)
	while cb != 0:
		pi.set_PWM_dutycycle(b3led, cb)
		cb = cb - 1
		time.sleep(fade_gap)




def out_fade(fade_gap):
	st0 = 0
	st1 = 0
	aa = 0
	ab = 255
	ba = 0
	bb = 255
	ca = 0
	cb = 255
	#fade_gap = 0.003

	while aa != 255:
		pi.set_PWM_dutycycle(b3led, aa)
		aa = aa + 1
		time.sleep(fade_gap)
		if aa == 127:
			st0 = 1
		if st0 == 1:
			pi.set_PWM_dutycycle(b2led, ba)
			pi.set_PWM_dutycycle(b4led, ba)
			ba = ba + 1
	while ab != 0:
		pi.set_PWM_dutycycle(b3led, ab)
		ab = ab - 1
		pi.set_PWM_dutycycle(b1led, ca)
		pi.set_PWM_dutycycle(b5led, ca)
		ca = ca + 1
		time.sleep(fade_gap)
		if st0 == 1:
			pi.set_PWM_dutycycle(b2led, ba)
			pi.set_PWM_dutycycle(b4led, ba)
			ba = ba + 1
			if ba == 255:
				st0 = 0
		elif st0 == 0:
			pi.set_PWM_dutycycle(b2led, bb)
			pi.set_PWM_dutycycle(b4led, bb)
			bb = bb - 1

			
	while bb != 0:
		pi.set_PWM_dutycycle(b2led, bb)
		pi.set_PWM_dutycycle(b4led, bb)
		bb = bb - 1
		time.sleep(fade_gap)
	while cb != 0:
		pi.set_PWM_dutycycle(b1led, cb)
		pi.set_PWM_dutycycle(b5led, cb)
		cb = cb - 1
		time.sleep(fade_gap)


def ltr(fade_gap):
	st0 = 0
	st1 = 0
	aa = 0
	ab = 255
	ba = 0
	bb = 255
	ca = 0
	cb = 255
	da = 0
	db = 255
	ea = 0
	eb = 255
	#fade_gap = 0.005

	while aa != 127:
		pi.set_PWM_dutycycle(b1led, aa)
		aa = aa + 1
		time.sleep(fade_gap)
	
	while aa != 255:
		pi.set_PWM_dutycycle(b1led, aa)
		aa = aa + 1
		pi.set_PWM_dutycycle(b2led, ba)
		ba = ba + 1
		time.sleep(fade_gap)
	
	while ab != 127:
		pi.set_PWM_dutycycle(b1led, ab)
		ab = ab - 1
		pi.set_PWM_dutycycle(b2led, ba)
		ba = ba + 1
		pi.set_PWM_dutycycle(b3led, ca)
		ca = ca + 1
		time.sleep(fade_gap)
		
	while ab != 0:
		pi.set_PWM_dutycycle(b1led, ab)
		ab = ab - 1
		pi.set_PWM_dutycycle(b2led, bb)
		bb = bb - 1
		pi.set_PWM_dutycycle(b3led, ca)
		ca = ca + 1
		pi.set_PWM_dutycycle(b4led, da)
		da = da + 1
		time.sleep(fade_gap)
		
	while cb != 127:
		pi.set_PWM_dutycycle(b2led, bb)
		bb = bb - 1
		pi.set_PWM_dutycycle(b3led, cb)
		cb = cb - 1
		pi.set_PWM_dutycycle(b4led, da)
		da = da + 1
		pi.set_PWM_dutycycle(b5led, ea)
		ea = ea + 1
		time.sleep(fade_gap)
		
	while db != 127:
		pi.set_PWM_dutycycle(b3led, cb)
		cb = cb - 1
		pi.set_PWM_dutycycle(b4led, db)
		db = db - 1
		pi.set_PWM_dutycycle(b5led, ea)
		ea = ea + 1
		time.sleep(fade_gap)

	while eb != 127:
		pi.set_PWM_dutycycle(b4led, db)
		db = db - 1
		pi.set_PWM_dutycycle(b5led, eb)
		eb = eb - 1
		time.sleep(fade_gap)
		
	while eb != 0:
		pi.set_PWM_dutycycle(b5led, eb)
		eb = eb - 1
		time.sleep(fade_gap)

			
		


def rtl(fade_gap):
	st0 = 0
	st1 = 0
	aa = 0
	ab = 255
	ba = 0
	bb = 255
	ca = 0
	cb = 255
	da = 0
	db = 255
	ea = 0
	eb = 255
	#fade_gap = 0.003

	while aa != 127:
		pi.set_PWM_dutycycle(b5led, aa)
		aa = aa + 1
		time.sleep(fade_gap)
	
	while aa != 255:
		pi.set_PWM_dutycycle(b5led, aa)
		aa = aa + 1
		pi.set_PWM_dutycycle(b4led, ba)
		ba = ba + 1
		time.sleep(fade_gap)
	
	while ab != 127:
		pi.set_PWM_dutycycle(b5led, ab)
		ab = ab - 1
		pi.set_PWM_dutycycle(b4led, ba)
		ba = ba + 1
		pi.set_PWM_dutycycle(b3led, ca)
		ca = ca + 1
		time.sleep(fade_gap)
		
	while ab != 0:
		pi.set_PWM_dutycycle(b5led, ab)
		ab = ab - 1
		pi.set_PWM_dutycycle(b4led, bb)
		bb = bb - 1
		pi.set_PWM_dutycycle(b3led, ca)
		ca = ca + 1
		pi.set_PWM_dutycycle(b2led, da)
		da = da + 1
		time.sleep(fade_gap)

		
	while cb != 127:
		pi.set_PWM_dutycycle(b4led, bb)
		bb = bb - 1
		pi.set_PWM_dutycycle(b3led, cb)
		cb = cb - 1
		pi.set_PWM_dutycycle(b2led, da)
		da = da + 1
		pi.set_PWM_dutycycle(b1led, ea)
		ea = ea + 1
		time.sleep(fade_gap)
		
	while db != 127:
		pi.set_PWM_dutycycle(b3led, cb)
		cb = cb - 1
		pi.set_PWM_dutycycle(b2led, db)
		db = db - 1
		pi.set_PWM_dutycycle(b1led, ea)
		ea = ea + 1
		time.sleep(fade_gap)

	while eb != 127:
		pi.set_PWM_dutycycle(b2led, db)
		db = db - 1
		pi.set_PWM_dutycycle(b1led, eb)
		eb = eb - 1
		time.sleep(fade_gap)


	while eb != 0:
		pi.set_PWM_dutycycle(b1led, eb)
		eb = eb - 1
		time.sleep(fade_gap)


def pulse(fade_gap):

	pwmdc = 0
	#fade_gap = 0.003

	while pwmdc != 255:
		pi.set_PWM_dutycycle(b1led, pwmdc)
		pi.set_PWM_dutycycle(b2led, pwmdc)
		pi.set_PWM_dutycycle(b3led, pwmdc)
		pi.set_PWM_dutycycle(b4led, pwmdc)
		pi.set_PWM_dutycycle(b5led, pwmdc)
		pwmdc = pwmdc + 1
		time.sleep(fade_gap)

	while pwmdc != 0:
		pi.set_PWM_dutycycle(b1led, pwmdc)
		pi.set_PWM_dutycycle(b2led, pwmdc)
		pi.set_PWM_dutycycle(b3led, pwmdc)
		pi.set_PWM_dutycycle(b4led, pwmdc)
		pi.set_PWM_dutycycle(b5led, pwmdc)
		pwmdc = pwmdc - 1
		time.sleep(fade_gap)

def dwr(fade_gap, loop, brightness):

	#fade_gap = 0.10
	#loop = 10
	while loop > 0:
		loop = loop - 1
		pi.set_PWM_dutycycle(EyeL, brightness)
		pi.set_PWM_dutycycle(EyeR, 0)
		time.sleep(fade_gap)
		pi.set_PWM_dutycycle(EyeR, brightness)
		pi.set_PWM_dutycycle(EyeL, 0)
		time.sleep(fade_gap)
		pi.set_PWM_dutycycle(EyeR, 0)

def eyes_on(brightness):
	pi.set_PWM_dutycycle(EyeR, brightness)
	pi.set_PWM_dutycycle(EyeL, brightness)

def eyes_off():
	pi.set_PWM_dutycycle(EyeR, 0)
	pi.set_PWM_dutycycle(EyeL, 0)

def buttons_on(brightness):
		pi.set_PWM_dutycycle(b1led, brightness)
		pi.set_PWM_dutycycle(b2led, brightness)
		pi.set_PWM_dutycycle(b3led, brightness)
		pi.set_PWM_dutycycle(b4led, brightness)
		pi.set_PWM_dutycycle(b5led, brightness)

def buttons_off():
	pwmdc = 0
	pi.set_PWM_dutycycle(b1led, pwmdc)
	pi.set_PWM_dutycycle(b2led, pwmdc)
	pi.set_PWM_dutycycle(b3led, pwmdc)
	pi.set_PWM_dutycycle(b4led, pwmdc)
	pi.set_PWM_dutycycle(b5led, pwmdc)
