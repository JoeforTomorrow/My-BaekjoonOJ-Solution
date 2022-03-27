import sys

lst = []

for i in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))

lst = lst[::-1]
std = lst[0]
res = 1

for i in range(0,len(lst)):
    if std < lst[i]:
        res += 1
        std = lst[i]

print(res)