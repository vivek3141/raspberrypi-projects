import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
G = int(sys.argv[1])
GPIO.setup(G,GPIO.OUT)
try:
	while(True):
		GPIO.output(G,1)
		time.sleep(0.5)
		GPIO.output(G,0)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
