n = int(input())
arr = list(map(int,input().split()))
stack = []
res = [0] * n
for i in range(n):
    m = arr[i]
    while stack and arr[stack[-1]] < m:
        stack.pop()
    if stack:
        res[i] = stack[-1] + 1
    stack.append(i)
for i in res:
    print(i, end=' ')