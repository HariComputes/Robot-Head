import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637

#CLK -> GPIO23 (Pin 16)
#Di0 -> GPIO24 (Pin 18)

disp = tm1637.TM1637(23, 24)
#Display.Clear()
#Display.SetBrightnes(1)


def clock(running):
	if running == 1:
		now = datetime.datetime.now()
		hours = now.strftime('%I')
		hour = int(hours)
	#	hour = now.hour
		minute = now.minute
		second = now.second
		currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]
		disp.set_values(currenttime)
		disp.set_doublepoint(second % 2)
		time.sleep(0.25)
	elif running == 0:
		disp.clear()
 