import sys
input = sys.stdin.readline

_, a = map(int,input().split())
lst = list(map(int,input().split()))
start = 0
end = max(lst)

res = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for i in lst:
        if i > mid:
            total += i - mid
    if total < a:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)