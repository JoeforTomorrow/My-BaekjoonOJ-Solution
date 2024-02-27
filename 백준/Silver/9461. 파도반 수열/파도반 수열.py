import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    lst = [1,1,1,2,2,3,4,5,7,9]
    if n > 10:
        for i in range(n-len(lst)):
            lst.append(lst[-1]+lst[-5])
        print(lst[-1])
    else:
        print(lst[n-1])