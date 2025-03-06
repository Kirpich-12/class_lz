#Class octagon whith сalculations and drawing
#Kirpich aka Deros. All rights reserved.
#============================================
from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt 


class Octagon:
    
    
    def __init__(self, st:int):
        self.st = st
        self.grad = 45
        self.k = 1 + sqrt(2)
        
    def  rad_opis(self) -> float: #радиус описанной окружности
        rad = sqrt((1 + sqrt(2))/((1 + sqrt(2)) - 1)) * self.st
        return rad
    
    def s_opis(self):
        s = pi * (self.rad_opis ** 2)
        return s
  
    def rad_vpis(self) -> float: #радиус вписанной окружности
        rad = (self.st / 2)* (1 + sqrt(2))
        return rad
    
    def s_opis(self):
        s = pi * (self.rad_vpis ** 2)
        return s
        
    def s(self):#площодь восьмиугольника
        s = 2 * (self.st ** 2) * (sqrt(2) + 1)
        print(f'Площадь восьмиугольника: {s}\n')
        
    def per(self):#Периметр восьмиугольника
        print(f'Периметр восьмиугольника: {self.st * 8}\n')
    
    def peaks(self) -> list:# Нахождение вершин
        peaks_x = []
        peaks_y =[]#Список вершин

        for i in range(8):#Создание списка вершин
            x = self.rad_opis() * cos((pi/8) + i * (pi/4))
            y = self.rad_opis() * sin((pi/8) + i * (pi/4))
            peaks_x.append(x)
            peaks_y.append(y)

        peaks_x.append(peaks_x[0])#Добавление первой координаты в конец, для того что бы соединить первую и последнюю вершину
        peaks_y.append(peaks_y[0])
        return peaks_x, peaks_y
    
    def paint(self):# Рисование фигур
        #Описанныая около восьмиугольника окружность
        circle1 = plt.Circle((0, 0 ), self.rad_opis(), color='b', fill=False)
        ax=plt.gca()
        ax.add_patch(circle1)

        #Впеисанная в восьмиугольник окружность
        circle2 = plt.Circle((0,0 ), self.rad_vpis(), color='r', fill=False)
        ax=plt.gca()
        ax.add_patch(circle2)

        #Восьмиугольник построенный по вершинам
        x,y = self.peaks()
        plt.plot(x, y, color = 'g')

        #Отображение
        plt.axis('scaled')
        plt.show()

    def __del__(self):
        print('Otagon has been deleted')
    

def left():

    zn = input('Введите сторону восьмиугольника\n')
    oct = Octagon(int(zn))
    print(oct.rad_opis())
    print(oct.rad_vpis())
    oct.s()
    oct.paint()
    print('============')
    x,y = oct.peaks()
    print(x)
    print(y)



def main():
    left()

if __name__ == '__main__':
    main()






