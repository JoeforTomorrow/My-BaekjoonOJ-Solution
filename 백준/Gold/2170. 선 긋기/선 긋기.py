import sys
input = sys.stdin.readline

lst = sorted([list(map(int,input().split())) for _ in range(int(input()))],key = lambda x:x[0])
res,n,m = 0,0,0
for i,j in lst:
    if not res:
        res = abs(j-i)
        n = i
        m = j
        continue
    if n <= i and m >= j:
        continue
    res += abs(j-i)
    if m > i:
        res -= abs(m-i)
    n=i
    m=j
print(res)