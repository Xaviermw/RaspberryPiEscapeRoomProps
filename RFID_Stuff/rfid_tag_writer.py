#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.cleanup()
reader = SimpleMFRC522()

try:
    text = input("Create tag name: ")
    print("Place tag on reader: ")
    reader.write(text)
    print("Now named: " + text)
    
finally:
    GPIO.cleanup()
