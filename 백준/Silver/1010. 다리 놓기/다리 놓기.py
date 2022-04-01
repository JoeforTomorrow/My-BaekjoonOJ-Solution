import sys
input = sys.stdin.readline
for i in range(int(input())):
    a, b = map(int,input().split())
    x = 1
    y = 1
    for i in range(b,b-a,-1):
        x *= i
    for i in range(1,a+1):
        y *= i
    print(int(x/y))