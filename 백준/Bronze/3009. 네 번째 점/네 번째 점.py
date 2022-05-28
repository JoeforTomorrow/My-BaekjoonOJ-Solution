lst = [[],[]]
for _ in range(3):
    a,b=map(int,input().split())
    lst[0].append(a)
    lst[1].append(b)
for i in lst[0]:
    if lst[0].count(i) == 1:
        n = i
for i in lst[1]:
    if lst[1].count(i) == 1:
        m = i
print(n, m)