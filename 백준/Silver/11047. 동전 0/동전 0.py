import sys
input = sys.stdin.readline
n,k=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
res = 0
while k != 0:
    for i in lst:
        if i <= k:
            k -= i
            res += 1
            break
print(res)