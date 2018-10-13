import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
G = int(sys.argv[1])
GPIO.setup(G, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
O = int(sys.argv[2])
GPIO.setup(O, GPIO.OUT)
try:
	while(True):
		if(GPIO.input(G) == 1):
			GPIO.output(O,1)
		else:
			GPIO.output(O,0)
except KeyboardInterrupt:
	GPIO.cleanup()
