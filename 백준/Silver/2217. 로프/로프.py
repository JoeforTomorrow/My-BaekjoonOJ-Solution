import sys

input=sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
res = []
for i in range(n):
    res.append(lst[i]*(i+1))
print(max(res))