cnt = 0
for i in range(1,int(input())+1):
    lst = list(map(int,str(i)))
    if len(lst) <= 2:
        cnt += 1
    elif len(lst) == 3:
        if lst[2]-lst[1] == lst[1] - lst[0]:
            cnt += 1
print(cnt)