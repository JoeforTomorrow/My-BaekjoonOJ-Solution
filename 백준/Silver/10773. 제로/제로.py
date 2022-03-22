k=int(input())
i = 0
res = 0
lst = []
while i != k:
    a = int(input())
    if a != 0:
        res += a
        lst.append(a)
        i += 1
    else:
        res -= lst[-1]
        lst.pop()
        i += 1
print(res)