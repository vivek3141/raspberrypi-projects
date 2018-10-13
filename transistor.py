import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
G = int(sys.argv[1])
GPIO.setup(G,GPIO.OUT)
try:
	while(True):
		GPIO.output(G,1)
		input()
		GPIO.output(G,0)
		input()
except KeyboardInterrupt:
	GPIO.cleanup()
