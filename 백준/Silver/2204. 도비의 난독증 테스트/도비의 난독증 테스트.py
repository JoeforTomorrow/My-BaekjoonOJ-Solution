res = []
while 1:
    lst=[]
    a=int(input())
    if a!= 0:
        for i in range(a):
            lst.append(input())
        lst.sort(key = lambda x : x.lower())
        res.append(lst[0])
    else:
        break
for i in res:
    print(i)