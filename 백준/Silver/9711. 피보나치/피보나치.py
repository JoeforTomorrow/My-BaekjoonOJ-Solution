import sys

input = sys.stdin.readline

for l in range(int(input())):
    n,m = map(int,input().split())
    if n != 1:
        x,y,z = 0,1,0
        for i in range(n-1):
            z = x+y
            x = y
            y = z
    else:
        z = 1
    print(f'Case #{l+1}: {z%m}')