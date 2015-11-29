# Import Libraries
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PINBuzzer = 22 # Set buzzer to pin 22

GPIO.setup(PINBuzzer,GPIO.OUT,initial=0)

def dot():
	GPIO.output(PINBuzzer,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(PINBuzzer,GPIO.LOW)
	time.sleep(.1)

def dash():
	GPIO.output(PINBuzzer,GPIO.HIGH)
	time.sleep(.3)
	GPIO.output(PINBuzzer,GPIO.LOW)
	time.sleep(.1)

def letterSpace():
	time.sleep(.2)

def wordSpace():
	time.sleep(.6)

def morseA(): # Morse code for A
	dot()
	dash()
	
def morseB() :
	dash()
	dot()
	dot()
	dot()

def morseC():
	dash()
	dot()
	dash()
	dot()

def morseD():
	dash()
	dot()
	dot()

def morseE():
	dot()

def morseF():
	dot()
	dot()
	dash()
	dot()

def morseG():
	dash()
	dash()
	dot()

def morseH():
	dot()
	dot()
	dot()
	dot()

def morseI():
	dot()
	dot()

def morseJ():
	dot()
	dash()
	dash()
	dash()

def morseK():
	dash()
	dot()
	dash()

def morseL():
	dot()
	dash()
	dot()
	dot()

def morseM():
	dash()
	dash()

def morseN():
	dash()
	dot()

def morseO():
	dash()
	dash()
	dash()

def morseP():
	dot()
	dash()
	dash()
	dot()

def morseQ():
	dash()
	dash()
	dot()
	dash()

def morseR():
	dot()
	dash()
	dot()

def morseS():
	dot()
	dot()
	dot()

def morseT():
	dash()

def morseU():
	dot()
	dot()
	dash()

def morseV():
	dot()
	dot()
	dot()
	dash()

def morseW():
	dot()
	dash()
	dash()

def morseX():
	dash()
	dot()
	dot()
	dash()

def morseY():
	dash()
	dot()
	dash()
	dash()

def morseZ():
	dash()
	dash()
	dot()
	dot()

def morse0():
	dash()
	dash()
	dash()
	dash()
	dash()

def morse1():
	dot()
	dash()
	dash()
	dash()
	dash()

def morse2():
	dot()
	dot()
	dash()
	dash()
	dash()

def morse3():
        dot()
        dot()
        dot()
        dash()
        dash()

def morse4():
        dot()
        dot()
        dot()
        dot()
        dash()

def morse5():
        dot()
        dot()
        dot()
        dot()
        dot()

def morse6():
        dash()
        dot()
        dot()
        dot()
        dot()

def morse7():
        dash()
        dash()
        dot()
        dot()
        dot()

def morse8():
        dash()
        dash()
        dash()
        dot()
        dot()

def morse9():
        dash()
        dash()
        dash()
        dash()
        dot()    

os.system('clear')
print "Morse Code"

loop_count = input("How many times would you like SOS to loop? ")

while loop_count > 0:
	loop_count = loop_count - 1
	morseS()
	letterSpace()
	morseO()
	letterSpace()
	morseS()
	wordSpace()

GPIO.cleanup()
