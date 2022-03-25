input()
lst = list(map(int,input().split()))
lst.sort()
res = 0
for i in range(len(lst)):
    res += sum(lst[0:i+1])
print(res)