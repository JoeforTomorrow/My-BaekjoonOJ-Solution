a, b = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
res=[]
for i in range(a):
    for j in range(i+1,a):
        for k in range( j+1,a):
            if (lst[i]+lst[j]+lst[k]) <= b:
                res.append((lst[i]+lst[j]+lst[k]))


print(max(res))