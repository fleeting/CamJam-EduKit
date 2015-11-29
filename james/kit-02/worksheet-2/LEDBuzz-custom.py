# Import Libraries
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Easy variables for GPIO pins.
LEDRed = 18
LEDBlue = 24
Buzzer = 22

# Set GPIO pins for output
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDBlue, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

def turnPinOn(pin):
	GPIO.output(pin, GPIO.HIGH)

def turnPinOff(pin):
	GPIO.output(pin, GPIO.LOW)

def blinkLED(pin, count=2):
	while count > 0:
		count = count - 1
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(0.3)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.3)

user_selection = 0
print "You control everything."
print "1: Turn on the red LED."
print "2: Turn on the blue LED."
print "3: Turn on the red and blue LEDs."
print "4: Sound the buzzer."
print "5: Turn on the red and blue LEDs and sound the buzzer."
print "6: Blink the red and blue LEDs."

while True:
	user_selection = input("Choose your option (1-6): ")
	print " "

	if user_selection == 1:
		print "The red LED is now on."
		turnPinOn(LEDRed)
		time.sleep(5)
		turnPinOff(LEDRed)

	if user_selection == 2:
		print "The blue LED is now on."
		turnPinOn(LEDBlue)
		time.sleep(5)
		turnPinOff(LEDBlue)

	if user_selection == 3:
		print "The red and blue LEDs are now on."
		turnPinOn(LEDRed)
		turnPinOn(LEDBlue)
		time.sleep(5)
		turnPinOff(LEDRed)
		turnPinOff(LEDBlue)

	if user_selection == 4:
		print "The buzzer is on...and is a little annoying."
		turnPinOn(Buzzer)
		time.sleep(.2)
		turnPinOff(Buzzer)
		time.sleep(.2)
		turnPinOn(Buzzer)
		time.sleep(.2)
		turnPinOff(Buzzer)

	if user_selection == 5:
		print "The red and blue LEDs and the buzzer are now on."
		turnPinOn(LEDRed)
		turnPinOn(LEDBlue)
		turnPinOn(Buzzer)
		time.sleep(.2)
		turnPinOff(Buzzer)
		time.sleep(4.8)
		turnPinOff(LEDRed)
		turnPinOff(LEDBlue)

	if user_selection == 6:
		print "The red and blue LEDs are now blinking."
		blinkLED(LEDRed, 4)
		blinkLED(LEDBlue)

	if user_selection == 0:
		print "Zero wasn't an option."
		break

	print " "
	print "########################################"
	print " "
	

GPIO.cleanup()
