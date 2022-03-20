lst1 = []
lst2 = []
M = int(input())
N = int(input())
for i in range(M, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            lst1.append(j)
    if len(lst1) == 2:
        lst2.append(i)
    lst1 = []
if len(lst2) == 0:
    print(-1)
else:
    print(sum(lst2))
    print(min(lst2))