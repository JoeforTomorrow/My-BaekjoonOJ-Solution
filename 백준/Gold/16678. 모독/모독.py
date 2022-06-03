import sys
input = sys.stdin.readline
lst = sorted([int(input()) for _ in range(int(input()))])
cnt = 0
res = 1
for i in lst:
    if i >= res:
        cnt += i - res
        res += 1
print(cnt)