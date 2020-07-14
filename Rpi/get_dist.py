from pirc522 import RFID
import signal
import RPi.GPIO as GPIO
import time
from time import sleep
class Sensor():
    def __init__(self,pins):
        self.pins=pins
        GPIO.setup(self.pins[0],GPIO.OUT)
        GPIO.setup(self.pins[1],GPIO.IN)
    def Get_dist(self,pins):
        self.pins=pins
        GPIO.output(self.pins[0],False)
        sleep(0.6)
        GPIO.output(self.pins[0],True)
        time.sleep(0.00001)
        GPIO.output(self.pins[0],False)
        while GPIO.input(self.pins[1])==False:
            start=time.time()
        while GPIO.input(self.pins[1])==True:
            end=time.time()
        sig_time=end-start
        distance=round(sig_time/0.000058,1)# or inches 0.000148
        if distance < 65:
            return True
        if distance > 200:
            return False
        sleep(1)