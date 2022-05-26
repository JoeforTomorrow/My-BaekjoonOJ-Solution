import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
arr1 = [0] * (n+1)

for _ in range(m):
    left, right, k = map(int,input().split())
    arr1[left-1] += k
    arr1[right] -= k

arr2 = [0] * (n+1)
arr2[0] = arr1[0]
for i in range(1,n+1):
    arr2[i] = arr2[i-1] + arr1[i]

for i in range(n):
    print(lst[i]+arr2[i], end=' ')