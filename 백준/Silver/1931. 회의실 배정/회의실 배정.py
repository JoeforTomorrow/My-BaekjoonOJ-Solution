import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    lst.append(list(map(int,input().split())))
lst.sort(key=lambda x : (x[1],x[0]))

cnt = 0
res = -1
for i in lst:
    if i[0] >= res:
        cnt += 1
        res = i[1]

print(cnt)