from scipy.io.wavfile import read
import numpy
import sys
import RPi.GPIO as GPIO
import pigpio
pi=pigpio.pi()
from time import sleep


ledpin = 11				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
#pi_pwm = GPIO.PWM(ledpin, 100)		#create PWM instance with frequency
#pi_pwm.start(100)

pi.set_PWM_dutycycle(ledpin, 100)

i = 0
p = 255

while i != 255:

	pi.set_PWM_dutycycle(ledpin, i)
	i = i + 1
	sleep(0.01)
	print(i)


while p != 0:
	pi.set_PWM_dutycycle(ledpin, p)
	p = p - 1
	sleep(0.01)
	print(p)


#sleep(5)

#pi.set_PWM_dutycycle(ledpin, 10)

#numpy.set_printoptions(threshold=sys.maxsize)

#a = read("lookdav.wav")
#print(a)
#array = numpy.array(a)
#print(array)

#import matplotlib.pyplot as plt
#from scipy.io import wavfile as wav
#from scipy.fftpack import fft
#import numpy as np
#rate, data = wav.read('lookdave.wav', rate=uint8)
#fft_out = fft(data)
#%matplotlib inline
#plt.plot(data, np.abs(fft_out))
#plt.show()