a = int(input())
lst = sorted(list(map(int,input().split())))
res = []
for i in range(a):
    res.append(lst[i::a][1])
print(max(res)-min(res))