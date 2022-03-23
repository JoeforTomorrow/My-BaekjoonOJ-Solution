a,b=map(int,input().split())
k=1
m=1
for i in range(0,b):
    k *= (a-i)
    m *= (i+1)
print(int(k/m))