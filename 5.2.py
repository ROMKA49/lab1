def q(a,b):
    if a>b:
        return a
    elif a==b:
        return "="
    else:
        return b

a,b=map(int, input().split())
print(q(a,b))
    
