import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

DESIRED_TAG = "test_just_wire_tag"
DESIRED_ID = 565462930062

reader = SimpleMFRC522()
correct_rfid = False

while correct_rfid == False:
    id, text = reader.read()
    print(id)
    print(text)
    if (text.strip() == DESIRED_TAG and id == DESIRED_ID):
        correct_rfid = True

print ("I Escaped!")
GPIO.cleanup()