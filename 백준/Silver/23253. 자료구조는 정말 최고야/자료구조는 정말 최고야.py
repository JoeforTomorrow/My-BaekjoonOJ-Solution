import sys

a,b = map(int,sys.stdin.readline().split())
lst = []
for i in range(b):
    input()
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort(key=lambda x : len(x), reverse=True)
find = 0
for i in range(len(lst)):

    res = lst[i].copy()
    res.sort(reverse=True)

    if lst[i] == res:
        find += 1
    else:
        print("No")
if find == len(lst):
    print("Yes")