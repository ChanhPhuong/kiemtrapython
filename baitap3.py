import math
from baitap2 import Shape

class Rect(Shape):
    def __init__(self ,x,y,dai,rong): 
        super().__init__(x,y)
        self.dai = dai
        self.rong = rong
    
    def chuVi(self):
        chuVi = (self.dai + self.rong) * 2
        return chuVi
    
    def dienTich(self):
        dienTich = self.dai * self.rong
        return dienTich

class Circle(Shape):
    def __init__(self,x,y,banKinh): 
        super().__init__(x,y)
        self.banKinh = banKinh

    def chuVi(self):
        chuVi = 2 * math.pi * self.banKinh
        return chuVi
    
    def dienTich(self):
        dienTich = self.banKinh * self.banKinh * math.pi
        return dienTich
    
class Triangle(Shape):
    def __init__(self ,x,y,a,b,c): 
        super().__init__(x,y)
        self.a = a
        self.b = b
        self.c = c

    def chuVi(self):
        chuVi = self.a + self.b + self.c
        return chuVi
        
    def dienTich(self):
        p = self.a + self.b + self.c / 2
        dienTich = math.sqrt(p* (p-self.a) * (p-self.b) * (p-self.c))
        return dienTich