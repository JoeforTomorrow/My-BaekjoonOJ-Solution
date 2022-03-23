a=input()
lst = []
for i in range(len(a)):
    lst.append(a[i])
lst.sort(reverse=True)
for i in lst:
    print(i,end='')