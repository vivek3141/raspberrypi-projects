
#print('hi')
# Import required Python libraries
import time
import RPi.GPIO as GPIO
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 16
GPIO_ECHO    = 23

GPIO.setup(12,GPIO.OUT)
# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger

GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
print "set false"
def measure():
# Allow sensor to settle
  time.sleep(0.1)
# Send 10us pulse to trigger
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time() 
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

# Calculate pulse length
  elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
  distance = elapsed * 34300
# That was the distance there and back so halve the value
  distance = distance / 2
  return distance
try:
  while(True):
    distance = measure()
    print(distance)
    if distance < 10:
      GPIO.output(12,True)
    if distance > 10:
      GPIO.output(12,False) 
except KeyboardInterrupt:
  GPIO.cleanup() 

# Reset GPIO settings


