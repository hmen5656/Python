# from pirc522 import RFID
# import signal
# import RPi.GPIO as GPIO
# import time
# from time import sleep
# from threading import Thread
# import asd
# from get_dist import Sensor
# GPIO.setwarnings(False)
# GPIO.cleanup()
# GPIO.setmode(GPIO.BOARD)
# rdr = RFID()
# util = rdr.util()
# util.debug = True
import sqlite3 as sq1
veritabani = 'Otopark.sqlite'

class Car_Control():  
    def __init__(self):
        self.hand=sq1.connect(veritabani)
        self.hand.cursor.execute("CREATE TABLE IF NOT EXISTS handicaped_info (kullanici_adi,kullanici_soyadi,plaka_no,giris_tarihi,cikis_tarihi,park_no)")
        self.hand.commit()
        self.hand.close()

        self.normal=sq1.connect(veritabani)
        self.normal.cursor.execute("CREATE TABLE IF NOT EXISTS non_handicaped_info (kullanici_adi,kullanici_soyadi,plaka_no,giris_tarihi,cikis_tarihi,park_no)")
        self.normal.commit()
        self.normal.close()

    def add_handicaped(self,kullanici_adi="",kullanici_soyadi="",plaka_no="",giris_tarihi="",cikis_tarihi="",park_no=""):
        kullanici_girisi = "INSERT INTO handicaped_info (kullanici_adi,kullanici_soyadi,plaka_no,giris_tarihi,cikis_tarihi,park_no) VALUES ('"+kullanici_adi+"','"+kullanici_soyadi+"','"+plaka_no+"','"+giris_tarihi+"','"+cikis_tarihi+"','"+park_no+"')"
        self.hand=sq1.connect(veritabani)
        self.hand.cursor.execute(kullanici_girisi)
        self.hand.commit()
        self.hand.close()

    def rm_handicaped(self,plaka):
        silme_kodu="DELETE FROM handicaped_info WHERE plaka_no='"+plaka+"'"
        self.hand=sq1.connect(veritabani)
        self.hand.cursor.execute(silme_kodu)
        self.hand.commit()
        self.hand.close()

    def add_normal(self,kullanici_adi="",kullanici_soyadi="",plaka_no="",giris_tarihi="",cikis_tarihi="",park_no=""):
        kullanici_girisi = "INSERT INTO non_handicaped_info (kullanici_adi,kullanici_soyadi,plaka_no,giris_tarihi,cikis_tarihi,park_no) VALUES ('"+kullanici_adi+"','"+kullanici_soyadi+"','"+plaka_no+"','"+giris_tarihi+"','"+cikis_tarihi+"','"+park_no+"')"
        self.normal=sq1.connect(veritabani)
        self.normal.cursor.execute(kullanici_girisi)
        self.normal.commit()
        self.normal.close()

    def rm_normal(self,plaka):
        silme_kodu="DELETE FROM non_handicaped_info WHERE plaka_no='"+plaka+"'"
        self.normal=sq1.connect(veritabani)
        self.normal.cursor.execute(silme_kodu)
        self.normal.commit()
        self.normal.close()

    def exit_car(self):
        #mark car as left the arking area
        pass

    def get_handicaped_plates(self):
        self.hand = sql.connect(veritabani)
        self.hand.cursor.execute("SELECT * FROM handicaped_info ORDER BY plaka_no")
        kullanicilar = self.hand.cursor.fetchall()
        for i in kullanicilar:
            for k in i:
                print(k,end=" ")
            print("")
        self.hand.close()
        return kullanicilar

    def get_parked_areas(self):
        #engelli yerlerindeki park alanlarinin id sini getir
        pass

    def check_distances(self):
        #mesafeleri kontrol et >100cm ise plakaya cikis yazdir
        pass
 