# Import libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PinPIR = 17

print "PIR Module Test (CTRL+C to exit)"

GPIO.setup(PinPIR, GPIO.IN)

current_state = 0
previous_state = 0

try:
	print "Waiting for PIR to settle..."
	print GPIO.input(PinPIR)
	
	while GPIO.input(PinPIR) == 1:
		current_state = 0

	print "  Ready"

	while True:
		current_state = GPIO.input(PinPIR)

		if current_state == 1 and previous_state == 0:
			print "  Motion detected!"
			previous_state = 1

		elif current_state == 0 and previous == 1:
			print "  Ready"
			previous_state = 0

		time.sleep(0.01)

except KeyboardInterrupt:
	print "  Quit"

	GPIO.cleanup()
