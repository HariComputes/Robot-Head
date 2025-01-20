from scipy.io.wavfile import read
import numpy
import sys
import RPi.GPIO as GPIO
import pigpio
pi=pigpio.pi()
from time import sleep


numpy.set_printoptions(threshold=sys.maxsize)

a = read("lookdav.wav")
#print(a)
array = numpy.array(a)
print(array)

#import matplotlib.pyplot as plt
#from scipy.io import wavfile as wav
#from scipy.fftpack import fft
#import numpy as np
#rate, data = wav.read('lookdave.wav', rate=uint8)
#fft_out = fft(data)
#%matplotlib inline
#plt.plot(data, np.abs(fft_out))
#plt.show()