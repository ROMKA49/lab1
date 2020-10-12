import random
lists = ['самовар', 'весна', 'лето']
k=random.choice(lists)
c=random.choice(k)
print(k[:k.index(c)]+'?'+k[k.index(c)+1:])

w=str(input('Попытайтесь угадать букву '))
if w==c:
    print('Вы угадали')
else:
    print('Вы не угадали')
