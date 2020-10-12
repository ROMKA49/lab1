def u(s,n):
    if len(s)>n:
        return s.upper()
    else:
        return s
s=str(input('Введите строку:'))
n=int(input('Введите значение:'))
print (u(s,n))
