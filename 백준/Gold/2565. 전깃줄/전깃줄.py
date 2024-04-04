import bisect
import sys

input = sys.stdin.readline

n = int(input())
all_lines = sorted([list(map(int, input().split())) for _ in range(n)])
lines = [line[1] for line in all_lines]
dp = [lines[0]]

for i in range(len(lines)):
    if lines[i] > dp[-1]:
        dp.append(lines[i])
    else:
        idx = bisect.bisect_left(dp, lines[i])
        dp[idx] = lines[i]

print(len(lines)-len(dp))