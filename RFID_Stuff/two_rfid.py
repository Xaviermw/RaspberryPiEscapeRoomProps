import RPi.GPIO as GPIO
from SimpleMFRC522_Pin_RST import SimpleMFRC522_Pin_RST


DESIRED_TAG = "test_just_wire_tag"
DESIRED_ID = 565462930062

try:
    reader_one = SimpleMFRC522_Pin_RST(pr=11)
    # reader_two = SimpleMFRC522_Pin_RST(pr=13) 17/27
    print("Reader One Mode: " + str(reader_one.READER.pin_mode))
    print("Reader One Pin RST: " + str(reader_one.READER.pin_rst))
    # print("Reader Two Mode: " + str(reader_two.READER.pin_mode))
    # print("Reader Two Pin RST: " + str(reader_two.READER.pin_rst))

    correct_rfid = False

    while correct_rfid == False:
        id_one, text_one  = reader_one.read()
        # id_two, text_two = reader_two.read()
        print("ID 1: " + str(id_one))
        # print("ID 2: " + str(id_two))
        
finally:
    GPIO.cleanup()
