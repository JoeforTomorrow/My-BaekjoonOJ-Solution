a,b = map(int,input().split())

c = b

if a != 0:
    lst = list(map(int,input().split()))
    cnt = 1
    for i in range(a-1):
        if b-lst[i] >= lst[i+1]:
            b = b-lst[i]
        else:
            b = c
            cnt += 1
else:
    cnt = 0

print(cnt)