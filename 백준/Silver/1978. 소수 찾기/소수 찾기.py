a=int(input())
lst=list(map(int,input().split()))
res=0
for i in lst:
    x=0
    for j in range(1,i+1):
        if i%j==0:
            x+=1
        if x >= 3:
            break
    if x == 2:
        res += 1
print(res)