import sys
input = sys.stdin.readline

lst = []
for i in range(int(input())):
    a,b=map(int,input().split())
    lst.append((a,b))
for i in lst:
    res = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            res += 1
    print(res,end=' ')