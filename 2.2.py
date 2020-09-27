def S(a,b):
    S=a*b
    P=2*(a+b)
    return S,P

a,b=map(int, input().split())

print(S(a,b))
