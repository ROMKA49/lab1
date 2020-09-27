def sec(N):
    D= (N-((N//3600)*3600))//60
    return D

N=int(input())
print(sec(N))
    
