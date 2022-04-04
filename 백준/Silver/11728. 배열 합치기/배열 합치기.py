import sys
input=sys.stdin.readline
input()
a=sorted(list(map(int,input().split()))+list(map(int,input().split())))
for i in a:
    print(i, end = ' ')