import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 16 
ECHO = 23

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, 0)
time.sleep(2)

GPIO.output(TRIG, 1)
time.sleep(0.00001)
GPIO.output(TRIG, 0)

while GPIO.input(ECHO)==0:
  start = time.time()

while GPIO.input(ECHO)==1:
  end = time.time()

pulse_duration = end - start 
distance = pulse_duration * 17150

print "Distance:",distance,"cm"

GPIO.cleanup()
