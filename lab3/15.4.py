class Point:
    x=0
    y=0
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y

point=Point()
point.setx(x=int(input("Введите x")))
point.sety(y=int(input("Введите y")))
print(point.getx())
print(point.gety())


