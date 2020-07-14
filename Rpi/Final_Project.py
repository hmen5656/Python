import cv2
import numpy as np
import os
from time import sleep
import DetectChars
import DetectPlates
import PossiblePlate
from pirc522 import RFID
import signal
import RPi.GPIO as GPIO
from threading import Thread
from get_dist import Sensor
import Functions as F
import entrance
H_P=2
N_P=4
Handicaped_Users=['']
Normal_Users=['']
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
rdr = RFID()
util = rdr.util()
util.debug = True
Car= F.Car_Control
entry_gate = entrance.Plates(0) #definition of entrance camera
exit_gate = entrance.Plates(1)#definition of exit camera
Plates=['']

def entrance_cam():
        plate_entry=entry_gate.take_pic() #gelen aracin plaka goruntusunu al
        i=Car.get_plates()#kayitli tum plakalari getir
        if plate_entry in i: #tum plakalar ile karsilastirma islemi yap eger engelli ise 
            if len(Handicaped_Users)==H_P: 
                if len(Normal_Users)==N_P:
                    print('Otopark Tamamem dolu')
                    #buraya kadar engelli ve normal park alanlari dolu ise
                    #otopark dolu mesajini kullaniciya bildir.
                else:
                    Normal_Users.append(plate_entry)
                    Car.add_handicaped(plate_entry)
                    ''' eger engelli park alani dolu ve normal park alaninda
                    bos alan varsa gelen araci oraya yonlendir
                    '''
            else:   
                #eger engelli park alaninda bos alan var ise
                # #gelen engelli aracini oraya yonlendir
                Handicaped_Users.append(plate_entry)
                Car.add_handicaped(plate_entry)
        else: # eger gelen arac engelli araci degilse 
            if len(Normal_Users)==N_P:
                    print('Otopark Tamamem dolu')
            else:
                Normal_Users.append(plate_entry)
                Car.add_normal(plate_entry)

def exit_cam():
        plate_exit=exit_gate.take_pic()
        j=Car.get_plates()
        
        if plate_exit in j:
            if plate_exit in Handicaped_Users:
                Handicaped_Users.remove[plate_exit]
            elif plate_exit in Normal_Users:
                Normal_Users.remove[plate_exit]    
            else:
                pass 
        elif plate_exit in  Normal_Users:
            Normal_Users.remove[plate_exit]   
        if len(Handicaped_Users)>0:
            park_no=get_parked_areas()
            check_distances(park_no)
                    
   
def Read_Card():   
        rdr.wait_for_tag()
        (error, data) = rdr.request()
        if not error:
            print("Kart Algilandi!")
            (error, uid) = rdr.anticoll()
        if not error:
            kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
            asd.take_pic()
            print(kart_uid)
        sleep(1)
  

card_th = Thread(target=lambda q, arg1: q.put(Read_Card()), args=(que,))
threcam_thad2.start()
threads_list.append(card_th)

entry_th = Thread(target=lambda q, arg1: q.put(entrance_cam(arg1)), args=(que,))
entry_th.start()
threads_list.append(entry_th)

exit_th = Thread(target=lambda q, arg1: q.put(exit_cam(arg1)), args=(que,))
exit_th.start()
threads_list.append(exit_th)

for t in threads_list:
    t.join()