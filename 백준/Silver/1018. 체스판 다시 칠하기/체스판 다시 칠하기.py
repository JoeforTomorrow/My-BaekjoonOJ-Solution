import sys

input = sys.stdin.readline

n,m=map(int,input().split())
lst=[input() for _ in range(n)]
res = []

for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0        
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if lst[k][l] != 'W':
                        w = w+1
                    if lst[k][l] != 'B':
                        b = b + 1
                else:
                    if lst[k][l] != 'B':
                        w = w+1
                    if lst[k][l] != 'W':
                        b = b + 1                        
        res.append(w)
        res.append(b)

print(min(res))