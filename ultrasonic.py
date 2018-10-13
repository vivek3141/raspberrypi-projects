import RPi.GPIO as GPIO
import time
GPIO_TRIGGER = 23
GPIO_ECHO = 16

def measure():
    time.sleep(0.1)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()
    time_elapsed = stop - start
    distance = time_elapsed * 34300/2
    return distance
def average():
    d1 = measure()
    time.sleep(0.1)
    d2 = measure()
    time.sleep(0.1)
    d3 = measure()
    time.sleep(0.1)
    return (d1 + d2 + d3)/3
                
GPIO.setmode(GPIO.BCM)



GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(17, GPIO.OUT)


GPIO.output(GPIO_TRIGGER,False)

try:
    while(True):
        distance = measure()
	print(distance)
        if distance < 10:
            GPIO.output(17, True)
        if distance > 10:
            GPIO.output(17, False)
except KeyboardInterrupt:
    GPIO.cleanup()


