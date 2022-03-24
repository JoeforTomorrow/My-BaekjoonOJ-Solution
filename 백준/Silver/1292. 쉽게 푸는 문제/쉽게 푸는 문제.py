a, b = map(int,input().split())

res_a = []
res_b = []

for i in range(1,a+1):
    for j in range(i):
        res_a.append(i)
        if len(res_a) == a:
            break
    if len(res_a) == a:
        break

for i in range(1,b+1):
    for j in range(i):
        res_b.append(i)
        if len(res_b) == b:
            break
    if len(res_b) == b:
        break

print(sum(res_b)-sum(res_a)+res_b[a-1])