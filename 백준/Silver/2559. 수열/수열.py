n,m = map(int,input().split())
lst = list(map(int,input().split()))
cnt = sum(lst[:m])
res = cnt
for i in range(m,n):
    cnt += lst[i] - lst[i-m]
    res = max(cnt,res)
print(res)