#Load Libraries
import os
import time
import RPi.GPIO as GPIO

#Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set up variables to store the pin numbers
LEDRed = 18
LEDYellow = 23
LEDGreen = 24

#Set the LED pins to output
GPIO.setup(LEDRed,GPIO.OUT)
GPIO.setup(LEDYellow,GPIO.OUT)
GPIO.setup(LEDGreen,GPIO.OUT)

#Setup variables for user input
led_choice = 0
count = 0
LEDChosen = 0
os.system('clear') #Clears the screen

print "Which LED would you like to blink?"
print "1: Red"
print "2: Yellow"
print "3: Green"

#Prints prompts to the screen and waits for input from the user
led_choice = input("Choose your option: ")
count = input("How many times would you like it to blink?: ")

#Set the LEDChosen variable depending on the LED choice
if led_choice == 1:
    print "You picked the Red LED"
    LEDChosen = LEDRed

if led_choice == 2:
    print "You picked the Yellow LED"
    LEDChosen = LEDYellow

if led_choice == 3:
    print "You picked the Green LED"
    LEDChosen = LEDGreen

# If a valid LED above is chosen, the value of LEDChosen will
# have been set to a value other than 0, so flash theLED
if LEDChosen<>0:
    while count > 0:
        GPIO.output(LEDChosen,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LEDChosen,GPIO.LOW)
        time.sleep(1)

        count = count –1

GPIO.cleanup()
