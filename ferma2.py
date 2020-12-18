import random
a = []

class pig():
    def __init__(self,name):
        print('Появилась свинья')
        self.name= name
        self.weight= random.randint(50,150)
        self.growth = random.randint(80,100)
        a.append(self.name)
    def korm(self):
        print("вы покормили свинью.")
    def naved(self):
        print('Вы навестили свинью с именем',self.name)
class horse():
    def __init__(self,name):
        print('Появилась лошадь')
        self.name= name
        self.weight= random.randint(50,150)
        self.growth = random.randint(80,100)
        a.append(self.name)
    def korm(self):
        print("вы покормили лошадь")
    def naved(self):
        print('Вы навестили лошадь с именем',self.name)
class cow():
    def __init__(self,name):
        print('Появилась корова')
        self.name= name
        self.weight= random.randint(50,150)
        self.growth = random.randint(80,100)
        a.append(self.name)
    def korm(self):
        print("вы покормили корову")
    def naved(self):
        print('Вы навестили корову с именем',self.name)

def main():
    choice = None
    while choice != 0:
        x = int(input("Добро пожаловать на ферму 1 - добавить животное ,2 - убрать животное,3 - список всех животных, любое другое число или буква - выход "))
        if x == 2:
            x = str(input("Введите имя животного "))
            for i in range(len(a)):
                if a[i] == x:
                    a.remove(a[i])
        elif x == 3:
            print(a)
        elif x == 1:
            choic = None
            while choic != 0:
                k = int(input("Кого хотите создать? 1 - свинья 2 - лошадь 3 - корова,любое другое число - перестать добавлять животных "))
                if k == 1:
                    aname = input("Дайте имя животному ")
                    ani = pig(aname)
                    choik = None
                    while choik != 0:
                        l = int(input("Чем хотите позаниматся? 1 - навестить , 2-покормить,4 - посмотреть информацию о животном, 3 - уйти "))
                        if l == 1:
                            ani.naved()
                        elif l == 2:
                            ani.korm()
                        elif l == 3:
                            choik = 0
                        elif l == 4:
                            print("Рост:", ani.growth)
                            print("Вес:", ani.weight)
                elif k==2:
                    aname = input("Дайте имя животному ")
                    ani = horse(aname)
                    choik = None
                    while choik != 0:
                        l = int(input("Чем хотите позаниматся? 1 - навестить , 2-покормить,4 - посмотреть информацию о животном, 3 - уйти "))
                        if l == 1:
                            ani.naved()
                        elif l == 2:
                            ani.korm()
                        elif l == 3:
                            choik = 0
                        elif l == 4:
                            print("Рост:", ani.growth)
                            print("Вес:", ani.weight)
                elif k == 3:
                    aname = input("Дайте имя животному ")
                    ani = cow(aname)
                    choik = None
                    while choik != 0:
                        l = int(input("Чем хотите позаниматся? 1 - навестить , 2-покормить,4 - посмотреть информацию о животном, 3 - уйти "))
                        if l == 1:
                            ani.naved()
                        elif l == 2:
                            ani.korm()
                        elif l == 3:
                            choik = 0
                        elif l == 4:
                            print("Рост:", ani.growth)
                            print("Вес:", ani.weight)
                else:
                    choic = 0

        else:
            choice = 0
main()





