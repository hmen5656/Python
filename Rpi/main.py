from pirc522 import RFID
import signal
import RPi.GPIO as GPIO
from time import sleep , time
from threading import Thread
import asd
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
Entrance=[7,11]
rdr = RFID()
util = rdr.util()
util.debug = True

def Read_Card():   
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    if not error:
        print("Kart Algilandi!")
        (error, uid) = rdr.anticoll()
    if not error:
        kart_uid = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])+str(uid[4])
        asd.take_pic()
        print(kart_uid)
    sleep(1)
#thread1 = Thread(target = Read_Card, args = ())
#thread1.start()


def Get_dist(gate_number,delay):
    GPIO.setup(gate_number[0],GPIO.OUT)
    GPIO.setup(gate_number[1],GPIO.IN)
    while True:
        GPIO.output(gate_number[0],False)
        sleep(0.6)
        GPIO.output(gate_number[0],True)
        sleep(0.00001)
        GPIO.output(gate_number[0],False)
        while GPIO.input(gate_number[1])==False:
            start=time()
        while GPIO.input(gate_number[1])==True:
            end=time()
        sig_time=end-start
        distance=round(sig_time/0.000058,1)# or inches 0.000148
        if distance < 65:
            asd.take_pic()
        if distance > 200:
            print('no object dedected in 2meter')
        sleep(delay)
    
#thread2 = Thread(target = Get_dist, args = ())
#thread2.start()

def Open_Gate(barrierno):
    GPIO.setup(barrierno, GPIO.OUT)
    pwm=GPIO.PWM(barrierno, 50)
    pwm.start(7)
    A=1./18.*(180)+2
    pwm.ChangeDutyCycle(A)
    pwm.stop()

while True:
    Read_Card()
    sleep(0.5)
    Get_dist()
    sleep(1)