a=input()
lst=[]
for i in range(0,len(a)):
    lst.append(a[i:])
lst.sort()
for i in lst:
    print(i)