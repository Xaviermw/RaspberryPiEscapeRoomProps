import RPi.GPIO as GPIO
import time
import smbus

address = 0x48
cmd = 0x40
###Can't Figure Out
input_1 = 0x41
bus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.HIGH)

def analogRead(chn):
    value = bus.read_byte_data(address, cmd+chn)
    return value

def analogWrite(value):
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        value = analogRead(0)
        valueTwo = analogRead(1)
#        valueThree = analogRead(2)
#        valueFour = analogRead(3)
        print("Value One: " + str(value))
        print("Value Two: " + str(valueTwo))
        
        #print("Value Three: " + str(valueThree))
        #print("Value Four: " + str(valueFour))
        print()
        if (value >  217 and valueTwo > 210):
                GPIO.output(17,GPIO.LOW)
        else:
                GPIO.output(17,GPIO.HIGH)
                
        time.sleep(0.5)
        
loop()


# while True:
#     # bus.write_byte(address, A0)
#     value = bus.read_byte(address)
#     #value2 = bus.read_byte(input_1)
#     print(value)
#     #print(value2)
#     if(value>155):
#         GPIO.output(17,GPIO.LOW)
#     else:
#         GPIO.output(17,GPIO.HIGH)
#     time.sleep(1)