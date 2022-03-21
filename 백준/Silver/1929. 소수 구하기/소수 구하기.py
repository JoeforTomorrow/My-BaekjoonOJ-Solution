M,N = map(int, input().split())
set1 = set(range(2, N+1)) - set(range(M))
for i in range(2, int(N**0.5)+1):
    set1 -= set(range(2*i, N+1, i))
lst1 = list(set1)
lst1.sort()
for j in lst1:
    print(j)