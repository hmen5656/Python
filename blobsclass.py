import  random

class blob:
    def __init__(self , color, x_baundary, y_baundary):
        self.size = random.randrange(4,20)
        self.color=color
        self.x_baundary = x_baundary
        self.y_baundary = y_baundary
        self.x = random.randrange(0, self.x_baundary)
        self.y = random.randrange(0, self.y_baundary)

    def move(self):
         self.movex = random.randrange(-2,3)
         self.movey = random.randrange(-2,3)
         self.x += self.movex
         self.y += self.movey

    def check_baunds(self):
         if self.x > self.x_baundary:
            self.x = self.x_baundary
         elif self.x < 0:
            self.x = 0

         if self.y > self.y_baundary:
            self.y = self.y_baundary
         elif self.y < 0:
            self.y = 0