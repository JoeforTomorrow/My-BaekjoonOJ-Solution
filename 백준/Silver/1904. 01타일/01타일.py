n = int(input())
dp = [0] * (n+1)
dp[1:3] = [1,2]
for k in range(3, n+1):
    dp[k] = (dp[k-1]+dp[k-2])%15746
print(dp[n])