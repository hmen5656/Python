import random
import time
class Dusman():
    def __init__(self,isim= "",kalan_can=1000,saldiri_gucu=20,kalan_mermi=150):
        self.harcanan_mermi=0
        self.saldiran_gucu=0
        self.atessayisi=0
        self.kalan_can = kalan_can
        self.isim = isim
        self.saldiri_gucu = saldiri_gucu
        self.kalan_mermi=kalan_mermi
        self.rakip="enemy"
    def saldir(self):
        if self.hayattami():
            print(self.isim, "attacking")
            self.harcanan_mermi = random.randrange(1, 10)
            self.kalan_mermi -= self.harcanan_mermi
            hdurum=False
            return (self.harcanan_mermi,self.saldiri_gucu,self.isim,hdurum)
        else:
             print(self.isim,"can't attack he is death")
             hdurum=True
             return (0,0,self.isim,hdurum)

    def saldirildi(self,saldiran):
        self.atessayisi = saldiran[0]
        self.saldiran_gucu = saldiran[1]
        self.rakip = saldiran[2]
        if (self.saldiri_gucu==0 and self.atessayisi==0) or saldiran[3]:
            print("couldn't attack")
        else:
             print(self.isim," : " , self.rakip,"attacking to us")
             self.kalan_can -= self.saldiran_gucu * self.atessayisi
    def mermi_durumu(self):
        if (self.kalan_mermi <= 0 ):
             print("rrun out of bullet!!!!")
             return True
        else:
            print(self.isim,"has been attaced by ",self.rakip,"and fired ",self.atessayisi , "bulllets")
    def hayattami(self):
        if (self.kalan_can <= 0):
            self.kalan_can=0
            print(self.isim,"death!!")
            return False
        else:
            print(self.isim,"alive!!",self.kalan_can,"survive point")
            return True
    def kullanılanmuhimmat(self):
        print(self.isim," fired ",self.harcanan_mermi, "bullets to", self.rakip)
        return self.harcanan_mermi
    def checkup(self):
        self.hayattami()
        self.mermi_durumu()
        self.kullanılanmuhimmat()
    def print(self):
        print("name ",self.isim,"--Life point ",self.kalan_can,"--Attack power",self.saldiri_gucu,"--Bullet",self.kalan_mermi)

"""
dusman1=Dusman()
dusman1.print()
dusman1.saldir()
print(dusman1.kalan_mermi)
time.sleep(2)
dusman1.saldir()
print(dusman1.kalan_mermi)
time.sleep(2)
dusman1.saldirildi(random.randrange(7,12),random.randrange(10,500))
if dusman1.hayattami():
    print(dusman1.kalan_can, "Canınız kaldı.", )
else:
    print(dusman1.kalan_can, "Can. Oyun bitti!!")

"""
##########################################################################
dusmanlar=[]
i=0
while i<10:
    rand_can=random.randrange(100,500)
    rand_mermi=random.randrange(100,200)
    rand_sgucu = random.randrange(20, 100)
    newenemy=Dusman(str(i+1)+".Soldier",rand_can,rand_sgucu,rand_mermi)
    dusmanlar.append(newenemy)
    i+=1
#########################################################################
for dusman in dusmanlar:
    dusman.print()
#########################################################################
i=0
while i<1:
    print("\nFirst attackt\n")
    saldirgan=random.randrange(10)
    savunan = random.randrange(10)
    gelenveri=dusmanlar[saldirgan].saldir()
    dusmanlar[savunan].saldirildi(gelenveri)
    dusmanlar[saldirgan].checkup()
    dusmanlar[savunan].checkup()

    print("\nSecond attack\n")

    gelenveri=dusmanlar[savunan].saldir()
    dusmanlar[saldirgan].saldirildi(gelenveri)
    dusmanlar[savunan].checkup()
    dusmanlar[saldirgan].checkup()
    i+=1
########################################################################


