# Import Libraries
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin 25 as an input pin
ButtonPin = 25
GPIO.setup(ButtonPin,GPIO.IN)

print "--------------------"
print " Button + GPIO "
print "--------------------"

print GPIO.input(ButtonPin)

while True:
	if GPIO.input(ButtonPin) == False:
		print "Button Pressed"
		print GPIO.input(ButtonPin)
		time.sleep(1)
	else:
		os.system('clear')
		print "Waiting for you to press a button..."

	time.sleep(0.5)
