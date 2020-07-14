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
import time
from time import sleep
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
Car= F.Car_Control()
entry_gate=entrance.Plates(0)
exit_gate=entrance.Plates(1)
Plates=['']
def entrance_cam(delay):
    # camera = cv2.VideoCapture(0)
    # return_value,image = camera.read()
    # blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()
    # if blnKNNTrainingSuccessful == False:                             
    #     print("\nerror: KNN traning was not successful\n") 
    #     pass
    # cv2.imwrite("1.png", image)
    # imgOriginalScene  = cv2.imread("1.png")
    # if imgOriginalScene is None:                            
    #     print("\nerror: image not read from file \n\n")  
    #     os.system("pause")                                  
    #     pass              
    # listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene) 
    # sleep(3)
    # if len(listOfPossiblePlates) == 0:                          
    #     print("\nPlaka bulunamadi\n")
    # else:                                                               
    #     listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)
    #     licPlate = listOfPossiblePlates[0]
    #     cv2.imshow("plaka", licPlate.imgPlate)           #plaka kismi kesilmis goruntu
    #     cv2.imwrite("plaka.png", licPlate.imgPlate)
    #     cv2.imshow("imgThresh", licPlate.imgThresh)
    #     if len(licPlate.strChars) == 0:                     # herhangi bir karakter okunmaz ise
    #         print("\nherhangi bir plaka tanimasi yapilamadi\n\n") 
    #         pass
    #     print("\nOkunan Plaka = " + licPlate.strChars + "\n")
    #     sleep(input(delay))
    #     camera.release()
    #     cv2.destroyAllWindows()
        plate=entrance.take_pic()
        i=Car.get_plates()
        if licPlate.strChars in i:
            if len.Handicaped_Users()>=H_P:
                if len.Normal_Users()>=N_P:
                    print('Otopark Tamamem dolu')
                else:
                    Normal_Users.append(licPlate.strChars)
                    Car.add_handicaped(licPlate.strChars)
            else:    
                Handicaped_Users.append(licPlate.strChars)
                Car.add_handicaped(licPlate.strChars)
        else:
            if len.Normal_Users()>=N_P:
                    print('Otopark Tamamem dolu')
                else:
                    Normal_Users.append(licPlate.strChars)
                    Car.add_normal(licPlate.strChars)

def exit_cam(delay):
    # camera_exit = cv2.VideoCapture(1)
    # return_value_exit,image_exit = camera_exit.read()
    # blnKNNTrainingSuccessful_exit = DetectChars.loadKNNDataAndTrainKNN()
    # if blnKNNTrainingSuccessful_exit == False:                             
    #     print("\nerror: KNN traning was not successful\n") 
    #     pass
    # cv2.imwrite("exit.png", image_exit)
    # imgOriginalScene_exit  = cv2.imread("exit.png")
    # if imgOriginalScene_exit is None:                            
    #     print("\nerror: image not read from file \n\n")  
    #     os.system("pause")                                  
    #     pass              
    # listOfPossiblePlates_exit = DetectPlates.detectPlatesInScene(imgOriginalScene) 
    # sleep(3)
    # if len(listOfPossiblePlates_exit) == 0:                          
    #     print("\nPlaka bulunamadi\n")
    # else:                                                               
    #     listOfPossiblePlates_exit.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)
    #     licPlate_exit = listOfPossiblePlates_exit[0]
    #     cv2.imshow("exit/plaka", licPlate_exit.imgPlate)           #plaka kismi kesilmis goruntu
    #     cv2.imwrite("exit/plaka.png", licPlate_exit.imgPlate)
    #     cv2.imshow("exit/imgThresh", licPlate_exit.imgThresh)
    #     if len(licPlate_exit.strChars) == 0:                     # herhangi bir karakter okunmaz ise
    #         print("\nherhangi bir plaka tanimasi yapilamadi\n\n") 
    #         pass
    #     print("\nOkunan Plaka = " + licPlate_exit.strChars + "\n")
    #     sleep(input(delay))
    #     camera.release()
    #     cv2.destroyAllWindows()
        licPlate_exit = exit_gate.take_pic()
        j=Car.get_plates()
        if licPlate_exit in j:
            if len.Handicaped_Users()>=H_P:
                if len.Normal_Users()>=N_P:
                    print('Otopark Tamamem dolu')
                else:
                    Normal_Users.remove(licPlate_exit)
                    Car.rm_handicaped(licPlate_exit)
            else:    
                Handicaped_Users.remove(licPlate_exit)
                Car.rm_handicaped(licPlate_exit)
        else:
            if len.Normal_Users()>=N_P:
                    print('Otopark Tamamem dolu')
                else:
                    Normal_Users.append(licPlate_exit)
                    Car.rm_normal(licPlate_exit)             
                    

                
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
  

cam_th = Thread(target=lambda q, arg1: q.put(Read_Card()), args=(que,))
threcam_thad2.start()
threads_list.append(cam_th)
card_th = Thread(target=lambda q, arg1: q.put(take_pic(arg1)), args=(que,'9'))
card_th.start()
threads_list.append(card_th)
for t in threads_list:
    t.join()