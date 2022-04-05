import sys
input= sys.stdin.readline
txt = input().strip()
res = 0
for n in range(int(input())):
    a = input().strip()
    for i in range(10):
        a = a[1:] + a[0]
        if txt in a:
            res += 1
            break
print(res)