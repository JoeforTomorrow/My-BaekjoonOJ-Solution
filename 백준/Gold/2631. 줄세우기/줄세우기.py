import bisect

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [arr[0]]

for _, i in enumerate(arr):
    if dp[-1] < i:
        dp.append(i)
    else:
        idx = bisect.bisect_left(dp, i)
        dp[idx] = i

print(n-len(dp))