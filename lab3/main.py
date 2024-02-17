#Написать программу, демонстрирующую работу с объектами
#двух типов T1 и T2, для чего создать систему соответствующих классов.
#Каждый объект должен иметь идентификатор (в виде произвольной строки
#символов) и одно или несколько полей для хранения состояния (текущего
#значения) объекта.
#Triangle, Tetragon move(), compare(T1 t1,T2 t2)
from math import sqrt


class Figure:
    def __init__(self, shape):
        self.shape = shape
class Point():
    def __init__(self, x,y):
        self.x=x
        self.y=y
        if type(self.x) in (int, float) and type(self.y) in (int, float):
            pass
        else:
            raise ValueError(f"Wrong data type for point coordinates :{self.__class__.__name__}!")
    def dist(self, p2):
        return sqrt(pow(p2.x-self.x,2)+pow(p2.y-self.y,2))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y=y
    def set_x(self,x):
        self.x=x

class Triangle(Figure):
    def __init__(self,shape, p):
        super().__init__(shape)
        self.p=p
        if (len(self.p)>3):
            raise ValueError(f"Wrong number of points for {self.__class__.__name__}!")

    def square(self):
        side=[]
        for i in range (2):
            side.append(self.p[i].dist(self.p[i+1]))
            if(i==1):
                side.append(self.p[i+1].dist(self.p[0]))
        per=sum(side)
        half_per=per/2
        return sqrt(half_per*(half_per-side[0])*(half_per-side[1])*(half_per-side[2]))

class Tetragon(Figure):
    def __init__(self, shape, p):
        super().__init__(shape)
        self.p = p
        if (len(self.p) > 4):
            raise ValueError(f"Wrong number of points for {self.__class__.__name__}!")
    def square(self):
        side = []
        for i in range(3):
            side.append(self.p[i].dist(self.p[i + 1]))
            if (i == 2):
                side.append(self.p[i + 1].dist(self.p[0]))
        triangles=[]
        tr1=[]
        tr1.append(self.p[0])
        tr1.append(self.p[1])
        tr1.append(self.p[2])
        tr2 = []
        tr2.append(self.p[0])
        tr2.append(self.p[2])
        tr2.append(self.p[3])
        trian1 = Triangle(1, tr1)
        trian2 = Triangle(2, tr2)

        return trian1.square()+trian2.square()
def move(T1):
        x=3
        y=5
        for i in range(len(T1.p)):
         p[i].set_y(y+p[i].get_y())
         p[i].set_x(x+p[i].get_x())

        tr1=[]
        for i in range(len(T1.p)):
         tr1.append(p[i])

        return T1


def prin(T1):
        print("Points", T1.__class__.__name__, T1.shape, " : ")
        for i in range(len(T1.p)):
            print("x:",p[i].get_x(),"y:",p[i].get_y())





def compare(T1, T2):
    if T1.square()>T2.square():
        print("Square ", T1.__class__.__name__," : ", T1.shape, " >", T2.shape)
    elif T1.square()<T2.square():
        print("Square ", T1.__class__.__name__," : ", T1.shape, " < ", T2.shape)
    else:
        print("The squares are equal")




p=[]
p.append(Point(0,5))
p.append(Point(5,0))
p.append(Point(0,0))
tr1=Triangle(1,p)
prin(tr1)
#move() сдвигает фигуру на 3 по х и на 5 по у
move(tr1)
prin(tr1)
p=[]
p.append(Point(0,7))
p.append(Point(7,0))
p.append(Point(1,1))
tr2=Triangle(2,p)
prin(tr2)
#move() сдвигает фигуру на 3 по х и на 5 по у
move(tr2)
prin(tr2)
p=[]
p.append(Point(0,5))
p.append(Point(5,0))
p.append(Point(0,0))
p.append(Point(5,5))
tet1=Tetragon(1,p)
prin(tet1)
#move() сдвигает фигуру на 3 по х и на 5 по у
move(tet1)
prin(tet1)
p=[]
p.append(Point(0,7))
p.append(Point(7,0))
p.append(Point(1,1))
p.append(Point(7,7))
tet2=Tetragon(2,p)
prin(tet2)
#move() сдвигает фигуру на 3 по х и на 5 по у
move(tet2)
prin(tet2)
compare(tr1,tr2)
compare(tet1,tet2)

