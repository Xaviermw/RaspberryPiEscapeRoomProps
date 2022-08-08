import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

GPIO.output(24,GPIO.HIGH)
print("LED on")
time.sleep(2)
GPIO.output(24,GPIO.LOW)
print ("LED off")
