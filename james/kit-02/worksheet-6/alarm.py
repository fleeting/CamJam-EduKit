# Import libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PinPIR = 17
PinRedLED = 18
PinBlueLED = 24
PinBuzzer = 22

print "PIR Module Test (CTRL+C to exit)"

GPIO.setup(PinPIR, GPIO.IN)
GPIO.setup(PinRedLED, GPIO.IN)
GPIO.setup(PinBlueLED, GPIO.IN)
GPIO.setup(PinBuzzer, GPIO.IN)

current_state = 0
previous_state = 0

try:
	print "Waiting for PIR to settle..."

	while GPIO.input(PinPIR) == 1:
		current_state = 0

	print "  Ready"

	while True:
		current_state = GPIO.input(PinPIR)

		if current_state == 1 and previous_state == 0:
			print "  Motion detected!"

			for x in range(0,3):
				GPIO.output(PinBuzzer, GPIO.HIGH)
				GPIO.output(PinRedLED, GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(PinRedLED, GPIO.LOW)
				GPIO.output(PinBlueLED, GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(PinBlueLED, GPIO.LOW)
				GPIO.output(PinRedLED, GPIO.LOW)
				time.sleep(0.5)

			previous_state = 1

		elif current_state == 0 and previous == 1:
			print "  Ready"
			previous_state = 0

		time.sleep(0.01)

except KeyboardInterrupt:
	print "  Quit"

	GPIO.cleanup()
