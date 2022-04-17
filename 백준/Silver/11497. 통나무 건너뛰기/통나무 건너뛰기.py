import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    lst = list(map(int,input().split()))
    lst.sort()
    print(max([ lst[i+2] - lst[i] for i in range(len(lst)-2) ]))