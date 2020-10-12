import random

print("Угадай число")

k=random.randint(1,10)
n=0
while k!=n:
    u=str(input('Выйти? для выхода написать выход ' ))
    if u=='выход':
        break
    else:
        n=int(input())
        if n>k:
            print('больше задуманного')
        elif n==k:
            print('вы угадали')
            break
        else:
            print('меньше задуманного')
