import sys

a,b = map(int,sys.stdin.readline().split())
c = 1
for i in range(b):
    sys.stdin.readline()
    lst=list(map(int,sys.stdin.readline().split()))
    if c == 0:
        pass
    else:
        res = lst.copy()
        res.sort(reverse=True)
        if lst != res:
            c = 0
        else:
            c = 1
print("Yes") if c==1 else print("No")