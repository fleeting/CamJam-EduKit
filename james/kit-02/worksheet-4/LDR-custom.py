# Import Libraries
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PinLDR = 27
LEDRed = 18
LEDBlue = 24

GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDBlue, GPIO.OUT)

def turnPinOn(pin):
	GPIO.output(pin, GPIO.HIGH)
	
def turnPinOff(pin):
	GPIO.output(pin, GPIO.LOW)

def ReadLDR():
	LDRCount = 0
	GPIO.setup(PinLDR, GPIO.OUT)
	GPIO.output(PinLDR, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(PinLDR, GPIO.IN)
	while (GPIO.input(PinLDR) == GPIO.LOW):
		LDRCount += 1
	return LDRCount

while True:
	current_ldr = ReadLDR()
	print current_ldr

	if current_ldr <= 2000:
		# High Light
		turnPinOn(LEDRed)
		turnPinOff(LEDBlue)
		
		print "Detecting high levels of light."

	if current_ldr >= 2001:
		# Low Light
		turnPinOn(LEDBlue)
		turnPinOff(LEDRed)

		print "Detecting low levels of light."

	print " "
	print "########################################"
	print " "

	time.sleep(1)
	
except KeyboardInterrupt:
	print "Quitting..."

	GPIO.cleanup()
