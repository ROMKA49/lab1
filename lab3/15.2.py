class Animal:
  name=""
  def eat(self):
     print("Ням ням")
  def setName(self, newName):
     self.name = newName
  def getName(self):
     return self.name
  def makeNoise(self):
     print(self.name + " говорит Гррр")
  def __init__(self,newName):
     self.name=newName
     print("Родилось животное " + self.name)

mycat=Animal("Ирис")
mycat.eat()
print(mycat.getName())
mycat.setName("Пушок")
print(mycat.getName())
mycat.makeNoise()
