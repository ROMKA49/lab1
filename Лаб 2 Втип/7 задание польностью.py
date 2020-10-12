n=int(input('Что нужно сделать задаче 7.1 соответствует значение 1,7.2 - 2 и т.д'))
import math
import random

if n == 1:
    a,b,c=map(int,input('Введите a,b,c').split())
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
elif n == 2:
    print(round (math.pi,2))
elif n == 3:
    x=int(input('Введите x'))
    print(math.sqrt(1-(math.sin(x)**2)))
elif n == 4:
    x=int(input('Компьютер загадал чилсо от 1 до 3,попытайтесь его угадать'))
    if x==random.randint(1,3):
        print('Вы угадали')
    else:
        print('Вы не угадали')
elif n == 5:
    x=int(input('Введите x'))
    def h(x):
        return x**4 + 4**x
    print(h(x))
elif n == 6:
    x,y=map(int,input('Введите x,y').split())
    z=(x+((2+y)/x**2))/(y + 1/math.sqrt(x**2+10))
    q=2.8*math.sin(x)+math.fabs(y)
    print (z,q)
elif n == 7:
    x=float(input('Введите x'))
    if 0.2 <= x <= 0.9:
        print(math.sin(x))
    else:
        print(1)
elif n == 8:
    x=random.randint(1,6)
    y=random.randint(1,6)
    print('У первого игрока',x)
    print('У второго игрока',y)
    if x>y:
        print('У первого игрока больше')
    else:
        print('У второго игрока больше')
        
    
        

    
    
