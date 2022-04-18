import sys
input = sys.stdin.readline
lst = []
for i in range(int(input())):
    lst.append(tuple(map(int,input().split())))
lst.sort(key=lambda x : x[1])
cnt = 0
res = 1000001
for i, j in lst:
    cnt += i
    res = min(res, j-cnt)
    if j < cnt:
        res = -1
        break
print(res)