x=int(input("Введите количество игр "))
for i in range(x):
    n=int(input("Количество секторов "))
    k=int(input("Номер черной мишени "))
    a=[]
    max=-100
    if (k == -1):
       for i in range(n):
           a.append(int(input()))
       for i in range(n):
           sum = 0
           for j in range(n):
               d=i+j
               if d > n-1:
                   d=d-n
               sum = sum + a[d]
               if sum > max:
                    max=sum
       print(max)
    else:
        for i in range(n):
            a.append(int(input()))
        a[k]=min(a)
        if a[k]>0:
            a[k]=0
        for i in range(n):
            sum = 0
            for j in range(n):
                d = i + j
                if d > n - 1:
                    d = d - n
                sum = sum + a[d]
                if sum > max:
                    max = sum
        print(max)






