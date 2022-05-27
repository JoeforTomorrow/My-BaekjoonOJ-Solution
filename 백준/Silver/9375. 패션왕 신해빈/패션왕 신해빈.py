import sys
input = sys.stdin.readline

for _ in range(int(input())):
    items={}
    for _ in range(int(input())):
        n,m=input().split()
        if m not in items:
            items[m] = 1
        else:
            items[m] += 1
    cnt = 1
    for i in list(items.values()):
        cnt *= (i+1)
    print(cnt-1)