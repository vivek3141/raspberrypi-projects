import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 16
ECHO = 23

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(2)

GPIO.output(TRIG,1)

time.sleep(0.0001)

GPIO.output(TRIG,0)

while(GPIO.input(ECHO) == 0):
	start = time.time()

while(GPIO.input(ECHO) == 1):
	stop = time.time()

time_elapsed = stop - start

distance = time_elapsed * 17000

print(distance + "cm")
