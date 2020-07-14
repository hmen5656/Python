import cv2
import numpy as np
import os
from time import sleep
import DetectChars
import DetectPlates
import PossiblePlate

class Plates():
    def __init__(self,camera_no):
        self.N_Car=0
        self.camera_no = camera_no

    def take_pic():
        camera = cv2.VideoCapture(self.camera_no)
        return_value,image = camera.read()
        blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()
        if blnKNNTrainingSuccessful == False:                               
            print("\nerror: KNN traning was not successful\n")  
            pass
        cv2.imwrite("1.png", image)
        imgOriginalScene  = cv2.imread("1.png")
        if imgOriginalScene is None:                           
            print("\nerror: image not read from file \n\n") 
            os.system("pause")                                 
            pass              
        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)
        sleep(2)
        
        if len(listOfPossiblePlates) == 0:                          
            print("\nPlaka bulunamadi\n")
        else:                                                               
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)
            licPlate = listOfPossiblePlates[0]
            #cv2.imshow("plaka", licPlate.imgPlate)           
            cv2.imwrite("{}plate.png".format(licPlate.strChars), licPlate.imgPlate)
            cv2.imwrite("{}car.png".format(licPlate.strChars), image )
            if len(licPlate.strChars) == 0:                    
                print("\nherhangi bir plaka tanimasi yapilamadi\n\n") 
                pass
            print("\nOkunan Plaka = " + licPlate.strChars + "\n")
            sleep(delay)
            camera.release()
            cv2.destroyAllWindows()
            self.N_Car = self.N_Car + 1
            return licPlate.strChars

    def get_carnumber():
        return self.camera_no
        
    